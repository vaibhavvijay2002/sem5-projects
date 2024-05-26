import React,{useState} from "react";
import axios from "axios";
import makeToast from "../Toaster/toaster";
import { withRouter } from "react-router";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min";
import Logo from '../images/logo.png'
import {useParams} from 'react-router-dom';

function CheckBalancePage(props) {
  const {cardno} = useParams();
  const [account, setAccount] = useState({});


  const getbalance = () => {


    axios
      .post("http://localhost:8000/user/checkbalance", {
        cardno
      })
      .then((response) => {
        setAccount(response.data.account);
        
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

  getbalance()

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
                  <span className="Tagline-Top Tagline">Balance</span>
                </div>

                    <div className="row ser-button">
                    <div className="col-sm-5 ser-button">
                        <span className="input-label">
                          Available Balance 
                        </span>
                    </div>
                    <div className="col-sm-2 ser-button"></div>
                    <div className="col-sm-5 ser-button">
                    <button className="right-sbutton" onClick={()=>{props.history.push("/dashboard/"+cardno)}}>Services</button>
                    </div>
                    </div>

                    <div className="row ser-button">
                    <div className="col-sm-5 ser-button">
                    <span className="input-label Tagline disp-data">
                          Rs. {account.balance} 
                        </span>
                    </div>
                    <div className="col-sm-2 ser-button"></div>
                    <div className="col-sm-5 ser-button">
                    <button className="right-sbutton" onClick={()=>{props.history.push("/withdraw/"+cardno)}}>Withdraw</button>
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

export default withRouter(CheckBalancePage);
