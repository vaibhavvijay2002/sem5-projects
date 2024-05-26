import React from "react";
import { useState, useEffect } from 'react';
import axios from "axios";
import makeToast from "../Toaster/toaster";
import { withRouter } from "react-router";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min";
import Logo from '../images/logo.png'
import {useParams} from 'react-router-dom';

function WithdrawOtherPage(props) {


  const {cardno} = useParams();
  const amountRef = React.createRef();

  const withdraw = () => {
    const amount = amountRef.current.value;
    
    if(amount>=100 && amount % 100 == 0){
      axios
      .post("http://localhost:8000/user/withdraw", {
        cardno,
        amount
      })
      .then((response) => {
        makeToast("success", response.data.message);
        props.history.push("/dashboard/"+ cardno);
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
    makeToast("error","Enter The Amount In Multiple Of 100's");
  }

    }
    
    
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
                <span className="Tagline-Top Tagline">Withdraw</span>
                </div>

                    <div className="row ser-button">
                    <div className="col-sm-7 ser-button">
                    <span className="input-label Tagline" htmlFor="name">Enther the Amount To Withdraw</span>
                    </div>
                    
                    <div className="col-sm-5 ser-button">
                    <button className="right-sbutton" onClick={withdraw}>Withdraw</button>
                    </div>
                    </div>

                    <div className="row ser-button">
                    <div className="col-sm-7 ser-button">
                    <input
                        className="form-control input-box"
                            type="text"
                            name="cardno"
                            placeholder="Amount"
                            ref={amountRef}
                        />
                    </div>
                    <div className="col-sm-5 ser-button">
                    <button className="right-sbutton" onClick={()=>{props.history.push("/dashboard/"+cardno)}}>Cancel</button>
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

export default withRouter(WithdrawOtherPage);
