import React, { FormEvent, useEffect, useState } from "react";
import EncounterApi from "../utils/apiWrappers";
import { CardGroup } from "react-bootstrap";
import { render } from "react-dom";

function Triage({uuid} : {uuid:any}) {
  const [triageFetched, setTriageFetched] = useState(false);
  const [triageClass, setTriageClass] = useState();
  const [followUpCode,setFollowUpCode] = useState();

  useEffect(() => {
    getTriage()
  }, []);
  
  useEffect(() => {
    window.scrollTo(0, document.body.scrollHeight);
  }, [triageFetched]);

  const getTriage = async () => {
    const api = new EncounterApi(uuid);
    try {
      const response = await api.generateTriage();

      setTriageClass(response['data']['triage_class']);
      setFollowUpCode(response['data']['follow_up_code']);

      setTriageFetched(true);
    } catch (error) {
      console.log(error);
    }
  };

  const renderTriage = () => {
    var headerText: string;
    var descriptionText: string;

    if (triageClass === 1) {
      headerText = "Visit emergency department or call 112"
      descriptionText = `Based on the symptoms you have described, we recommend that you visit the emergency department or call 112. To make the process smoother, please save the code we are providing you. You will need to present it upon arrival at the center.`
    }
    else if (triageClass === 2) {
      headerText = "Visit your local after-hour medical center"
      descriptionText = `Based on the symptoms you have described, we recommend that you
      visit a nearby after-hours medical center. To make the process
      smoother, please save the code we are providing you. You will need
      to present it upon arrival at the center.`
    }
    else {
      headerText = "No need to visit immediate medical attention"
      descriptionText = `Based on the symptoms you have described, it seems that your condition is not severe. Therefore, it may be appropriate to wait until regular medical hours to seek care. If your symptoms worsen or if you have any concerns, please do not hesitate to seek medical attention as soon as possible.`
    }



    return (
      <div className="card my-4 text-center shadow">
          <div className="p-3 p-lg-5 pt-lg-3">
            <h1 className="display-4 fw-bold lh-1 text-body-emphasis">
              {headerText}
            </h1>
            <p className="lead">
              {descriptionText}
            </p>
            <div className="d-grid gap-2 d-md-flex justify-content-md-center mb-4 mb-lg-3">
              <div className="alert alert-primary" role="alert">
                <strong>
                  <h1>{followUpCode}</h1>
                </strong>
              </div>
            </div>
          </div>
        </div>
    )
  };

  return (
    <>
      {triageFetched ? (
        renderTriage()
      ) : (
        <div className="text-center my-2">
          <div className="spinner-border text-primary" role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
        </div>
      )}
    </>
  );
}


export default Triage;
