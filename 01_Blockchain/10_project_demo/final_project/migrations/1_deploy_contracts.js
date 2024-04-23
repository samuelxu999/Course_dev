var TokenData = artifacts.require("./TokenData.sol");


module.exports = function(deployer) {
	deployer.deploy(TokenData);
};
