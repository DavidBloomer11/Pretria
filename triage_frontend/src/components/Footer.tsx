import React from "react";

function Footer() {
  return (
    <>
      <footer className="footer shadow">
        <div className="container">
          <div className="row justify-content-start align-items-center g-2">
            <div className="col">
            <span className="mb-3 mb-md-0 text-muted">© 2023 PreTria</span>
            </div>
            <div className="col">
              <ul className="nav justify-content-center">
                <li className="nav-item">
                  <a href="/dashboard/login/" className="nav-link px-2 text-muted">
                    Doctor login
                  </a>
                </li>
                <li className="nav-item">
                  <a href="/features/" className="nav-link px-2 text-muted">
                    Features
                  </a>
                </li>
                <li className="nav-item">
                  <a href="/faq/" className="nav-link px-2 text-muted">
                    FAQs
                  </a>
                </li>
                <li className="nav-item">
                  <a href="/about/" className="nav-link px-2 text-muted">
                    About
                  </a>
                </li>
              </ul>
            </div>
            <div className="col"></div>
          </div>
        </div>
      </footer>
    </>
  );
}

export default Footer;
