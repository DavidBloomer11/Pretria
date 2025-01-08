import React from "react";

function Header() {
  return (
    <>
      <header className="d-flex flex-wrap align-items-center justify-content-center justify-content-md-between py-3 mb-4 border-bottom bg-white">
        <div className="container">
          <div className="row">
            <div className="col">
              <a
                href="/"
                className="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-decoration-none fw-bold text-body"
              >
                <img src="static/react-images/logo.png" alt="Your Logo" width="33" height="40" className="me-2" />
                <span className="fs-4">PreTria</span>
              </a>
            </div>

            <div className="col text-end mx-4">
              <button type="button" className="btn btn-outline-primary me-2">
                <a href="/dashboard/login/" className="text-decoration-none">Login</a>
              </button>
            </div>
          </div>
        </div>
      </header>
    </>
  );
}

export default Header;
