import React from "react";
import axios from "axios";
import makeToast from "../Toaster/toaster";
import { withRouter } from "react-router";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min";
import Logo from '../images/logo.png'
import {useParams} from 'react-router-dom';

function ChangePhonePage(props) {
  const {cardno} = useParams();

  const phoneRef = React.createRef();
  const oldphoneRef = React.createRef();

  const changephone = () => {

    const oldphone = oldphoneRef.current.value;
    const newphone = phoneRef.current.value;

    if(oldphone.length == 10 && newphone.length == 10){
      axios
      .post("http://localhost:8000/user/changephone", {
        cardno,
        oldphone,
        newphone
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
      makeToast("error", "Phone Number Should Be 10 Digits");
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

                <span className="Tagline-Top Tagline">Change Phone Number</span>
                </div>

                    <div className="row ser-button">
                    <div className="col-sm-7 ser-button">
                   
                        <span className="input-label" htmlFor="oldphone">Old Phone Number</span>
                        <input
                        className="form-control input-box"
                            type="text"
                            name="oldphone"
                            placeholder="+91 XXXXX XXXXX"
                            ref={oldphoneRef}
                        />
                   
                    </div>
                    
                    <div className="col-sm-5 ser-button">
                    <button className="right-sbutton" onClick={changephone}>Update</button>
                    </div>
                    </div>

                    <div className="row ser-button">
                    <div className="col-sm-7 ser-button">
                   
                        <span className="input-label" htmlFor="newphone">New Phone Number</span>
                        <input
                        className="form-control input-box"
                            type="text"
                            name="newphone"
                            placeholder="+91 XXXXX XXXXX"
                            ref={phoneRef}
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

export default withRouter(ChangePhonePage);
