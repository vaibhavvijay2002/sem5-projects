import React from "react";
import axios from "axios";
import makeToast from "../Toaster/toaster";
import { withRouter } from "react-router";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min";
import Logo from '../images/logo.png'
import {useParams} from 'react-router-dom';

function ChangePinPage(props) {
  const {cardno} = useParams();
  const oldpinRef = React.createRef();
  const pinRef = React.createRef();

  const changepin = () => {
    const oldpin = oldpinRef.current.value;
    const newpin = pinRef.current.value;

    if(oldpin.length == 4 && newpin.length == 4)
    {
      axios
      .post("http://localhost:8000/user/changepin", {
        cardno,
        oldpin,
        newpin
      })
      .then((response) => {
        makeToast("success", response.data.message);
        props.history.push("/dashboard/"+cardno);
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
      makeToast("error", "ATM Pin Should Be 4 Digits");
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

                <span className="Tagline-Top Tagline">Change ATM Pin</span>
                </div>

                    <div className="row ser-button">
                    <div className="col-sm-7 ser-button">
                   
                        <span className="input-label" htmlFor="oldpin">Enter The Old Pin</span>
                        <input
                        className="form-control input-box"
                            type="password"
                            name="oldpin"
                            placeholder="Pin : XXXX"
                            ref={oldpinRef}
                        />
                   
                    </div>
                    
                    <div className="col-sm-5 ser-button">
                    <button className="right-sbutton" onClick={changepin}>Update</button>
                    </div>
                    </div>

                    <div className="row ser-button">
                    <div className="col-sm-7 ser-button">
                   
                        <span className="input-label" htmlFor="newpin">Enter The New Pin</span>
                        <input
                        className="form-control input-box"
                            type="password"
                            name="newpin"
                            placeholder="Pin : XXXX"
                            ref={pinRef}
                        />
                   
                    </div>
                    <div className="col-sm-5 ser-button">
                    <button className="right-sbutton" onClick={()=>{props.history.push("/dashboard/"+cardno)}}>Services</button>
                    </div>
                    </div>

                    <div className="row ser-button">
                    <div className="col-sm-5 ser-button">
                        
                    </div>
                    <div className="col-sm-2 ser-button"></div>
                    <div className="col-sm-5 ser-button">
                    <button className="right-sbutton" onClick={()=>{props.history.push("/login")}}>Exit</button>
                    </div>
                    </div>

            </div>

            <div className="col-sm-0.5"></div>

          </div>
        </div>
      
    </>
  );
}

export default withRouter(ChangePinPage);
