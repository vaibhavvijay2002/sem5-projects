import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";

import LoginPage from "./pages/loginPage";
import DashboardPage from "./pages/dashboardPage";
import IndexPage from "./pages/indexPage";
import CheckBalancePage from "./pages/checkBalancePage";
import DepositPage from "./pages/depositPage"; 
import WithdrawPage from "./pages/withdrawPage";
import AboutPage from "./pages/aboutPage";
import ChangePinPage from "./pages/changePinPage";
import ChangePhonePage from "./pages/changePhonePage";
import AccountInfoPage from "./pages/accountInfoPage";
import WithdrawOtherPage from "./pages/withdrawOtherPage";

function App() {
  return (
    <BrowserRouter>
      <Switch>
        <Route path="/" component={IndexPage} exact />
        <Route
          path="/login"
          component={LoginPage}
          exact
        />

        <Route
          path="/dashboard/:cardno"
          component={DashboardPage}
          exact
        />

        <Route
          path="/about"
          component={AboutPage}
          exact
        />

        <Route
          path="/checkbalance/:cardno"
          component={CheckBalancePage}
          exact
        />

        <Route
          path="/changephone/:cardno"
          component={ChangePhonePage}
          exact
        />
        <Route
          path="/changepin/:cardno"
          component={ChangePinPage}
          exact
        />
        <Route
          path="/withdraw/:cardno"
          component={WithdrawPage}
          exact
        />
        <Route
          path="/withdrawother/:cardno"
          component={WithdrawOtherPage}
          exact
        />
        <Route
          path="/deposit/:cardno"
          component={DepositPage}
          exact
        />
        <Route
          path="/accountinfo/:cardno"
          component={AccountInfoPage}
          exact
        />
      </Switch>
    </BrowserRouter>
  );
}
export default App;
