import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min';
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min";
import Logo from '../images/logo.png'
import {useParams} from 'react-router-dom';

const DashboardPage = (props) => {

    const {cardno} = useParams();

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

                <div className="row one-row-gap"><span className="Tagline-Top Tagline"> Services</span></div>

                

                    <div className="row ser-button">
                    <div className="col-sm-5 ser-button">
                        <button className="left-sbutton" onClick={()=>{props.history.push("/accountinfo/"+cardno)}}>Account Info</button>
                    </div>
                    <div className="col-sm-2 ser-button"></div>
                    <div className="col-sm-5 ser-button">
                    <button className="right-sbutton" onClick={()=>{props.history.push("/withdraw/"+cardno)}}>Withdraw</button>
                    </div>
                    </div>

                    <div className="row ser-button">
                    <div className="col-sm-5 ser-button">
                        <button className="left-sbutton" onClick={()=>{props.history.push("/changepin/"+cardno)}}>Change ATM Pin</button>
                    </div>
                    <div className="col-sm-2 ser-button"></div>
                    <div className="col-sm-5 ser-button">
                    <button className="right-sbutton" onClick={()=>{props.history.push("/deposit/"+cardno)}}>Deposit</button>
                    </div>
                    </div>

                    <div className="row ser-button">
                    <div className="col-sm-5 ser-button">
                        <button className="left-sbutton" onClick={()=>{props.history.push("/changephone/"+cardno)}}>Change Phone No</button>
                    </div>
                    <div className="col-sm-2 ser-button"></div>
                    <div className="col-sm-5 ser-button">
                    <button className="right-sbutton" onClick={()=>{props.history.push("/checkbalance/"+cardno)}}>Balance Enquiry</button>
                    </div>
                    </div>

            </div>

            <div className="col-sm-0.5"></div>

          </div>
        </div>
      
    </>

    )
};

export default DashboardPage;
