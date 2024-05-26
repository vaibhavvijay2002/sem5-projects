import React from "react";
import axios from "axios";
import makeToast from "../Toaster/toaster";
import { withRouter } from "react-router";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min";
import Logo from '../images/logo.png'


function LoginPage(props) {
  const cardnoRef = React.createRef();
  const pinRef = React.createRef();

  const loginUser = () => {
    const cardno = cardnoRef.current.value;
    if(cardno.length == 16)
    {
      const pin = pinRef.current.value;
      if(pin.length == 4){
        axios
        .post("http://localhost:8000/user/login", {
          cardno,
          pin,
        })
        .then((response) => {
          makeToast("success", response.data.message);
          localStorage.setItem("U_Token", response.data.token);
          props.history.push("/dashboard/" + cardno);
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
        
      }
      else{
        makeToast("error","Pin Should Cantain 4 Digits !");
      }

      
    }
    else{
      makeToast("error","Card No Should Cantain 16 Digits !");
    }
    
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
                <img src={Logo} className="shift-logo" alt="" />
                </div>
                <div className="col-sm-4 logo-lane"></div>
                </div>

                <div className="row one-row-gap">
                  <span className="Tagline-Top Tagline"> Welcome </span>
                </div>

                    <div className="row ser-button">
                    <div className="col-sm-7 ser-button">
                   
                        <span className="input-label" htmlFor="cardno">Card Number</span>
                        <input
                        className="form-control input-box"
                            type="text"
                            name="cardno"
                            placeholder="Your Card No : XXXX XXXX XXXX XXXX"
                            ref={cardnoRef}
                        />
                   
                    </div>
                    
                    <div className="col-sm-5 ser-button">
                    <button className="right-sbutton" onClick={loginUser}>ENTER</button>
                    </div>
                    </div>

                    <div className="row ser-button">
                    <div className="col-sm-7 ser-button">
                    
                        <span className="input-label" htmlFor="pin">ATM PIN</span>
                        <input
                        className="form-control input-box"
                            type="password"
                            name="pin"
                            placeholder="Your ATM Pin"
                            ref={pinRef}
                        />
                    
                    </div>
              
                    <div className="col-sm-5 ser-button">
                    <button className="right-sbutton" onClick={()=>{
                      cardnoRef.current.value = "";
                      pinRef.current.value = "";
                    }}>CLEAR</button>
                    </div>
                    </div>

                    <div className="row ser-button">
                    <div className="col-sm-5 ser-button">
                        
                    </div>
                    <div className="col-sm-2 ser-button"></div>
                    <div className="col-sm-5 ser-button">
                    <button className="right-sbutton" onClick={()=>{props.history.push("/about")}}>ABOUT</button>
                    </div>
                    </div>

            </div>

            <div className="col-sm-0.5"></div>

          </div>
        </div>
      
    </>
  );
}

export default withRouter(LoginPage);
