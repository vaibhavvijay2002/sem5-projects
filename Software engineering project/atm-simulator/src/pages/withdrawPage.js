import React from "react";
import { useState, useEffect } from 'react';
import axios from "axios";
import makeToast from "../Toaster/toaster";
import { withRouter } from "react-router";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min";
import Logo from '../images/logo.png'
import {useParams} from 'react-router-dom';

function WithdrawPage(props) {

  const {cardno} = useParams();

  const [amount, setAmount] = useState(0);

  
  

  const withdraw = () => {

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
                <span className="Tagline-Top Tagline">Withdraw</span>
                </div>

                    <div className="row ser-button">
                    <div className="col-sm-5 ser-button">
                        <button className="left-sbutton"  onClick={()=>{setAmount(500)}}>500</button>
                    </div>
                    <div className="col-sm-2 ser-button"></div>
                    <div className="col-sm-5 ser-button">
                    <button className="right-sbutton"  onClick={withdraw}>Enter</button>
                    </div>
                    </div>

                    <div className="row ser-button">
                    <div className="col-sm-5 ser-button">
                        <button className="left-sbutton" onClick={()=>{setAmount(1000)}}>1000</button>
                    </div>
                    <div className="col-sm-2 ser-button"></div>
                    <div className="col-sm-5 ser-button">
                    <button className="right-sbutton" onClick={()=>{props.history.push("/withdrawother/"+cardno)}}>Other Amount</button>
                    </div>
                    </div>

                    <div className="row ser-button">
                    <div className="col-sm-5 ser-button">
                        <button className="left-sbutton" onClick={()=>{setAmount(2000)}}>2000</button>
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

export default withRouter(WithdrawPage);
