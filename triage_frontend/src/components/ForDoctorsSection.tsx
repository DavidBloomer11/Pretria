import { useState } from "react";
import SymptomDescription from "./SymtpomDescription";

function ForDoctorsSection() {

  return (
    <>
          <div className="row mt-4 p-0 pb-0 pe-lg-0 pt-lg-5 align-items-center rounded-3 border shadow-lg bg-white">
  <div className="col-lg-5 p-0 overflow-hidden shadow-lg ms-lg-0">
    <img
      className="rounded-lg-3"
      src="src/assets/prototype.PNG"
      alt=""
      height="400"
    />
  </div>
  <div className="col-lg-6 offset-lg-1 p-3 p-lg-5 pt-lg-3">
    <h1 className="display-4 fw-bold lh-1 text-body-emphasis">
      For Patients
    </h1>
    <p className="lead">
      The worlds first fully NLP-powered pre-triage tool.
    </p>
    <p className="lead typed-text">For patients. For doctors</p>

    <div className="d-grid gap-2 d-md-flex justify-content-md-start mb-4 mt-4 mb-lg-3">
      <button
        type="button"
        className="btn btn-primary btn-lg px-4 me-md-2 fw-bold"
      >
        Start digital consultation
      </button>
    </div>
  </div>
</div>


        </>
  );
}

export default ForDoctorsSection;
