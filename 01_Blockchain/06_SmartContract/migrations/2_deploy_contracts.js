var Box = artifacts.require("./Box.sol");
var BoxPro = artifacts.require("./BoxPro.sol");


module.exports = function(deployer) {
	deployer.deploy(Box);
	deployer.deploy(BoxPro);
};
