import { useState, FormEvent } from "react";
import QuestionList from "./QuestionList";
import EncounterApi from "../utils/apiWrappers"

interface Question {
  id: number;
  question: string;
  answer_type: string;
  answer: string;
}



function SymptomDescription({uuid}:any) {

  const [questionListError, setQuestionListError] = useState(false)
  const [questionsFetched, setQuestionListFetched] = useState(false);
  const [questionList,setQuestionList] = useState([])
  const [spinner, setSpinner] = useState(false);
  

  // Function that handles submit
  const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
  
    setSpinner(true);
    const api = new EncounterApi(uuid);
  
    // get form data
    const formData = new FormData(event.target as HTMLFormElement);
    const symptoms = formData.get("symptoms") as string;
    const age = formData.get("age") as string;
    const gender = formData.get("gender") as string;
    

    //Update encounter info
    try {
      await api.update({
        'age' : parseInt(age),
        'gender' : gender,
        'description' : symptoms
      })

      // Fetch additional questions
      const response = await api.generateQuestions()

      //Map questions to questionlist
      console.log(response.data)

      const questionList = response.data.map((question: any) => {
        return {
          id: question.id,
          question: question.question,
          answer_type: question.answer_type,
          answer: ''
        };
      });
      
      setQuestionList(questionList);

      setQuestionListFetched(true)
      
      
      
    }
    catch {
      // Will throw an error
      setQuestionListError(true)
    }
    

    
    setSpinner(false);
  };
  



  return (
    <>
      <div className="card shadow">
        <div className="card-body">

          {questionListError ? (
            <div className="alert alert-danger" role="alert">
            Could not get enough information from the description of the symptoms, try again.
            </div>
          ) : null
          }
          
          

          <h1 className="display-6 fw-bold">Digital Consultation</h1>

          <form onSubmit={handleSubmit}>

            <label htmlFor="symptoms">Symptoms:</label>
            <textarea
              className="form-control my-2"
              id="symptoms"
              name="symptoms"
              rows={4}
              placeholder="Enter a description of symptoms"
            ></textarea>
            <label htmlFor="age">Age:</label>

            <input
              className="form-control my-2"
              type="number"
              id="age"
              name="age"
              placeholder="Enter your age"
              required
            />
            <label htmlFor="gender">Gender:</label>

            <select className="form-select my-2" id="gender" name="gender" required>
              <option value="male">Male</option>
              <option value="female">Female</option>
            </select>

            <input name="" id="" className="btn btn-outline-primary mt-2" type="submit" value="Next"/>
            

          </form>
        </div>
        </div>

        {spinner ? (
        <div className="text-center my-2">
          <div className="spinner-border text-primary" role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
        </div>
      ) : questionsFetched ? (
        
        <QuestionList questionList={questionList} uuid = {uuid} />
      ) : null}

    </>
  );
}
export default SymptomDescription;

