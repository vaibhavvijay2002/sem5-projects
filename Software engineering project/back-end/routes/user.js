const router = require('express').Router();
const {catchErrors} = require("../handlers/errorHanders");
const userController = require("../controllers/userController");

router.post("/login",catchErrors(userController.login));
router.post("/checkbalance",catchErrors(userController.checkBalance));
router.post("/accountinfo",catchErrors(userController.accountInfo));
router.post("/withdraw",catchErrors(userController.withdrawMoney));
router.post("/deposit",catchErrors(userController.depositMoney));
router.post("/changepin",catchErrors(userController.changePin));
router.post("/changephone",catchErrors(userController.changePhone));


module.exports = router;