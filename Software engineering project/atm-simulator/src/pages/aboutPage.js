import React from "react";
import axios from "axios";
import makeToast from "../Toaster/toaster";
import { withRouter } from "react-router";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min";
import Logo from '../images/logo.png'
import Prem from '../images/prem.jpg'
import Tushar from '../images/tusharj.jpeg'
import Vaibhav from '../images/vaibhav.jpeg'
import Thushar from '../images/thusharm.jpeg'

function AboutPage(props) {
  const cardnoRef = React.createRef();
  const pinRef = React.createRef();

  const about= () => {
    const cardno = cardnoRef.current.value;
    const pin = pinRef.current.value;

    axios
      .post("http://localhost:8000/user/login", {
        cardno,
        pin
      })
      .then((response) => {
        makeToast("success", response.data.message);
        localStorage.setItem("U_Token", response.data.token);
        props.history.push("/servies");
      })
      .catch((err) => {
        if (
          err &&
          err.response &&
          err.response.data &&
          err.response.data.message
        ) {
          makeToast("error", err.response.data.message);
        }
      });
  };
  return (
    <>
      
        <div class="container">
          <div className="row"></div>

          <div className="row main-box">
            <div className="col-sm-0.5"></div>

            <div className="col-sm-11 inner-box">
                
                <div className="row logo-lane">
                <div className="col-sm-4 logo-lane"></div>
                <div className="col-sm-4 logo-lane">
                <img onClick={()=>{props.history.push("/login")}} src={Logo} className="shift-logo" alt="" />
                </div>
                <div className="col-sm-4 logo-lane"></div>
                </div>

                <div className="row one-row-gap">
                <span className="Tagline-Top Tagline">Project</span>
                </div>
                <div className="row one-row-gap">
                <span className="prodesc">An ATM Simulator Application Built Using MERN Stack Technology.</span>
                </div>

                <div className="row">
                <span className="Tagline-Top Tagline team-tag">Team Description</span>
                </div>

                <div className="team row">

            <div className="teammember col-sm-2"></div>
            <div className="teammember col-sm-2">
                <img src={Tushar} className="memberpic" alt="" />
                <span className="membername">Tushar J</span>
                <p className="memberdes">Contributor</p>
            </div>

            <div className="teammember col-sm-2">
            <img src={Vaibhav} className="memberpic" alt="" />
                <span className="membername">Vaibhav Vijay</span>
                <p className="memberdes">Contributor</p>
            </div>

            <div className="teammember col-sm-2">
            <img src={Prem} className="memberpic" alt="" />
                <span className="membername">Prem Sagar</span>
                <p className="memberdes">Contributor</p>
            </div>

            <div className="teammember col-sm-2">
            <img src={Thushar} className="memberpic" alt="" />
                <span className="membername">Thushar M</span>
                <p className="memberdes">Contributor</p>
            </div>

            <div className="teammember col-sm-2"></div>
            </div>

            


            </div>

            <div className="col-sm-0.5"></div>

          </div>
        </div>
      
    </>
  );
}

export default withRouter(AboutPage);

        

            
