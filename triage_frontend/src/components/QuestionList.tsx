import React, { FormEvent, useEffect, useState } from "react";
import EncounterApi from "../utils/apiWrappers";
import Triage from "./Triage";

interface Question {
  id: number;
  question: string;
  answer_type: string;
  answer: string;
}

function QuestionList({ questionList, uuid }: { questionList: Question[], uuid:any }) {
  const [answeredQuestions, setAnsweredQuestions] = useState<Question[]>([]);
  const [count, setCount] = useState<number>(0);

  useEffect(() => {
    window.scrollTo(0, document.body.scrollHeight);
  }, [count]);

  const handleNextQuestion = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    // get form data
    const formData = new FormData(event.target as HTMLFormElement);
    const answer = formData.get("answer") as string;

    //Register answer in questionList
    questionList[count]["answer"] = answer;

    // Make PATCH request to register answer
    const api = new EncounterApi(uuid);

    try {
      await api.updateAnswer(
        {
          answer: answer,
        },
        questionList[count]["id"]
      );
    } catch {
      // Will throw an error
      console.log("error");
    }

    // Append the answered questions list
    setAnsweredQuestions([...answeredQuestions, questionList[count]]);
    setCount(count + 1);
  };

  const getCurrentQuestion = () => {
    const currentQuestion = questionList[answeredQuestions.length];
    if (currentQuestion.answer_type === "bool") {
      return (
        <select className="form-select my-2" id="answer" name="answer" required>
          <option value="yes">Yes</option>
          <option value="no">No</option>
        </select>
      );
    } else if (currentQuestion.answer_type === "int") {
      return (
        <input
          className="form-control my-2"
          type="number"
          id="answer"
          name="answer"
          required
        />
      );
    } else {
      return (
        <input
          className="form-control my-2"
          type="text"
          id="answer"
          name="answer"
          required
        />
      );
    }
  };



  return (
    <div id="questions-wrapper">
      {answeredQuestions.map((question, index) => (
        <div className="card mt-4 shadow" key={index}>
          <div className="card-body">
            <h5 className="card-title">{question.question}</h5>
            <p>{question.answer}</p>
          </div>
        </div>
      ))}
  
      { answeredQuestions.length < questionList.length ? (
        <div className="card mt-4 shadow" key={count} id={`question`}>
          <div className="card-body">
            <h5 className="card-title">
              {questionList[answeredQuestions.length].question}
            </h5>
            <form onSubmit={handleNextQuestion}>
              {getCurrentQuestion()}
              <button className="btn btn-outline-primary" type="submit">
                Next question
              </button>
            </form>
          </div>
        </div>
      ) : <Triage uuid= {uuid} />}
    </div>
  );
  
}

export default QuestionList;
