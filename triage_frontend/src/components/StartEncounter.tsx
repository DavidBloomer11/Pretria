import { useState } from "react";
import SymptomDescription from "./SymtpomDescription";
import EncounterApi from "../utils/apiWrappers";

function StartEncounter() {
  const [encounterStarted, setEncounterStart] = useState(false);
  const [uuid, setUuid] = useState("");
  // Button to start consultation
  const handleClick = async (event : any) => {
    // Create new consultation
    try {
      const api = new EncounterApi('')

      //Wait for data
      const data = await api.create();


      //Set state UUID
      setUuid(data['data']['uuid']);
    } catch (error) {
      console.error(error);
    }

    setEncounterStart(true);
  };

  return (
    <>
      {encounterStarted ? (
        <SymptomDescription uuid={uuid}></SymptomDescription>
      ) : (
        <>
          <div className="row mt-4 p-4 pb-0 pe-lg-0 pt-lg-5 align-items-center rounded-3 border shadow-lg bg-white">
            <div className="col-lg-6 p-3 p-lg-5 pt-lg-3">
              <h1 className="display-3 fw-bold lh-1 text-body-emphasis">
                PreTria
              </h1>
              <p className="lead">
                The worlds first fully NLP-powered pre-triage tool.
              </p >
              <p className="lead typed-text">For patients. For doctors.</p>

              <div className="d-grid gap-2 d-md-flex justify-content-md-start mb-4 mt-4 mb-lg-3">
                <button
                  type="button"
                  className="btn btn-primary btn-lg px-4 me-md-2 fw-bold"
                  onClick={handleClick}
                >
                  Start digital consultation
                </button>
                
              </div>
            </div>
            <div className="col-lg-5 offset-lg-1 p-0 overflow-hidden shadow-lg">
              <img
                className="rounded-lg-3"
                src="static/react-images/prototype.png"
                alt=""
                height="400"
              />
            </div>
          </div>
        </>
      )}
    </>
  );
}

export default StartEncounter;
