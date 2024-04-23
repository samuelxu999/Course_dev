// test/Box.test.js
// Load dependencies
const { expect } = require('chai');

// Start test block
describe('Token', function () {
  before(async function () {
    this.Token = await ethers.getContractFactory('Token');
  });

  beforeEach(async function () {
    this.token = await this.Token.deploy();
    await this.token.deployed();
  });

  // Test case
  it('query returns a value previously deposit', async function () {
    // save a value
    await this.token.deposit(1, 10);

    // Test if the returned value is the same one
    // Note that we need to use strings to compare the 256 bit integers
    expect((await this.token.query(1)).toString()).to.equal('10');
  });
  it('query returns a value after withdow', async function () {
    // save a value
    await this.token.deposit(1, 10);

    // subtract a value
    await this.token.withdraw(1, 5);

    // Test if the returned value is the same one
    // Note that we need to use strings to compare the 256 bit integers
    expect((await this.token.query(1)).toString()).to.equal('5');
  });
  // Test case
  it('query returns a policy previously saved', async function () {
    // save a value
    await this.token.set_policy(1, 'Test policy');

    // Test if the returned value is the same one
    // Note that we need to use strings to compare the 256 bit integers
    expect((await this.token.get_policy(1)).toString()).to.equal('Test policy');
  });
});
