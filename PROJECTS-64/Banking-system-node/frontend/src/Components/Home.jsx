import React from "react";
import bankImage from '../assets/bank.jpg';

function Home() {
  return (
    <section className="bg-light min-vh-100 d-flex align-items-center">
      <div className="container py-5">
        <div className="row align-items-center">
          {/* Left Content */}
          <div className="col-md-6 text-center text-md-start mb-4 mb-md-0">
            <h1 className="display-4 fw-bold text-dark">
              Welcome to <span className="text-success">MyBank</span>
            </h1>
            <p className="lead text-secondary mt-3">
              Manage your finances smartly with secure banking features, instant transfers, and powerful insights.
            </p>
            <div className="mt-4">
              <a href="#" className="btn btn-primary px-4 py-2 me-2 shadow-sm">
                Get Started
              </a>
              <a href="#" className="btn btn-outline-secondary px-4 py-2">
                Learn More
              </a>
            </div>
          </div>

          {/* Right Image */}
          <div className="col-md-6 text-center">
            <img
              src={bankImage}
              alt="Banking Illustration"
              className="img-fluid rounded shadow-sm"
              style={{ maxHeight: "400px" }}
            />
          </div>
        </div>
      </div>
    </section>
  );
}

export default Home;
