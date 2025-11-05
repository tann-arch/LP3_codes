// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Bank {
    // Mapping to store each user's balance
    mapping(address => uint256) private balances;

    // Event logs
    event Deposit(address indexed accountHolder, uint256 amount);
    event Withdraw(address indexed accountHolder, uint256 amount);

    // Deposit Ether into the bank
    function deposit() public payable {
        require(msg.value > 0, "Deposit amount must be greater than 0");
        balances[msg.sender] += msg.value;
        emit Deposit(msg.sender, msg.value);
    }

    // Withdraw Ether from the bank
    function withdraw(uint256 amount) public {
        require(amount > 0, "Withdraw amount must be greater than 0");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        payable(msg.sender).transfer(amount);

        emit Withdraw(msg.sender, amount);
    }

    // View current balance of the caller
    function getBalance() public view returns (uint256) {
        return balances[msg.sender];
    }
}







































Perfect, Shubham — this one’s a **Solidity smart contract for a simple decentralized Bank**, one of the most commonly asked practicals for blockchain students.
Let’s unpack it like a blockchain developer preparing for both theory *and* viva: with **deep EVM theory**, **line-by-line explanation**, **expected modifications**, and even **security & gas insights**.

---

## 🧭 THEORETICAL OVERVIEW

This **Bank** contract simulates a minimal version of a decentralized banking system on Ethereum.
Each user can:

* **Deposit** ETH into the contract.
* **Withdraw** their ETH.
* **Check** their current balance.

It relies on:

* **Mappings** to store user balances.
* **Payable functions** for ETH transfers.
* **Events** for transaction logging.
* **Transfer pattern** for secure withdrawals.

This is a foundational example for understanding **state management** and **Ether flow** in Ethereum smart contracts.

---

## 🧠 DEEP THEORY CONCEPTS USED

### 1. **Ethereum Accounts and Balances**

* Two account types:

  * **Externally Owned Account (EOA):** controlled by a private key (like MetaMask users).
  * **Contract Account:** controlled by smart contract code.

When EOAs send Ether to contracts via `deposit()`, that Ether is added to the **contract’s own balance** in the EVM.

`address(this).balance` gives total ETH in contract.

---

### 2. **Mapping (Storage Data Structure)**

`mapping(address => uint256)`

* Works like a hash table.
* Keys = user addresses
* Values = balances (in wei).
* Default value = `0` if not yet written.
* Stored in Ethereum **storage** (persistent, gas-costly).

Mappings don’t store keys, only values at keccak hash positions:

```
keccak256(h(key) . slot)
```

This means you can’t iterate over mappings — you must track keys separately if needed.

---

### 3. **Payable Functions**

Functions marked `payable` can receive Ether.
`msg.value` holds the amount of wei sent.
Without `payable`, a function will reject ETH sent to it.

Example:

```solidity
function deposit() public payable { ... }
```

The Ether sent is held in the **contract’s balance** (`address(this).balance`),
not automatically assigned to users — that’s why we manually add it in `balances[msg.sender]`.

---

### 4. **Events and Logs**

Events are a low-cost way to log information to the blockchain for **off-chain use**.
They are stored in transaction receipts, not contract storage, hence gas-cheaper.
`indexed` parameters allow efficient filtering via topics.

Example:

```solidity
event Deposit(address indexed accountHolder, uint256 amount);
```

Emitted during `deposit()` to track who sent how much.

---

### 5. **Ether Transfer Mechanics**

`payable(msg.sender).transfer(amount)` sends Ether back to the caller.

Ether transfer methods:

| Method                     | Gas limit | Throws on failure | Recommended use                   |
| -------------------------- | --------- | ----------------- | --------------------------------- |
| `.transfer()`              | 2300 gas  | Yes               | Safe, simple transfers            |
| `.send()`                  | 2300 gas  | No                | Must check return value           |
| `.call{value: amount}("")` | All gas   | No                | Flexible, used in modern patterns |

`transfer()` is safest for basic contracts, but can break if fallback consumes >2300 gas (EIP-1884).
So newer code prefers `call{value: amount}("")`.

---

### 6. **Reentrancy Attack Theory**

When transferring Ether to another contract, that contract’s fallback function might call back into your contract **before state updates finish**, exploiting it to drain funds.

In this Bank, we prevent that by:

* Updating balance **before** transferring ETH.

  ```solidity
  balances[msg.sender] -= amount;
  payable(msg.sender).transfer(amount);
  ```

  This is called **Checks-Effects-Interactions pattern** — a critical Solidity design pattern.

---

### 7. **Gas and Storage**

* Writing to mapping (`balances[msg.sender] += ...`) costs ~20,000 gas if new, 5,000 if updated.
* Reading (`balances[msg.sender]`) is free off-chain, but costs ~200 gas on-chain.
* Events are cheaper than storing data permanently in state.

---

### 8. **Security Best Practices**

* Use **require()** for input validation — prevents invalid transactions.
* Avoid leaving ETH stuck — always provide withdrawal mechanisms.
* Consider adding **ReentrancyGuard** for advanced versions.

---

## 🧩 LINE-BY-LINE EXPLANATION

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
```

Defines the license type and compiler version.
`^0.8.0` ensures safety with overflow/underflow checks (introduced in Solidity 0.8+).

---

```solidity
contract Bank {
```

Declares the contract named `Bank`.

---

```solidity
    mapping(address => uint256) private balances;
```

Maps each user address to their current balance.
`private` → cannot be read directly by external contracts, but you can expose it with a getter if needed.

---

```solidity
    event Deposit(address indexed accountHolder, uint256 amount);
    event Withdraw(address indexed accountHolder, uint256 amount);
```

Define events for logging deposits and withdrawals.
`indexed` makes them searchable in block explorers.

---

### Deposit Function

```solidity
    function deposit() public payable {
        require(msg.value > 0, "Deposit amount must be greater than 0");
        balances[msg.sender] += msg.value;
        emit Deposit(msg.sender, msg.value);
    }
```

* `msg.value` = Ether sent in wei.
* Ensures amount > 0.
* Adds to sender’s internal balance.
* Emits event to record deposit.
* `payable` allows function to receive ETH.

If user sends 2 ETH →
`balances[msg.sender] += 2 ether;`

---

### Withdraw Function

```solidity
    function withdraw(uint256 amount) public {
        require(amount > 0, "Withdraw amount must be greater than 0");
        require(balances[msg.sender] >= amount, "Insufficient balance");
```

Validates withdrawal amount and user’s balance.

```solidity
        balances[msg.sender] -= amount;
        payable(msg.sender).transfer(amount);
```

First deducts from user balance (**effects**)
Then sends Ether (**interaction**) → follows **Checks-Effects-Interactions** pattern.

```solidity
        emit Withdraw(msg.sender, amount);
    }
```

Logs withdrawal event.

---

### View Function

```solidity
    function getBalance() public view returns (uint256) {
        return balances[msg.sender];
    }
```

Returns the caller’s stored balance.
`view` → read-only, no gas when called externally (e.g., via MetaMask or frontend).

---

## 🧮 DRY RUN EXAMPLE

| User  | Action          | Ether | Result                  |
| ----- | --------------- | ----- | ----------------------- |
| Alice | deposit()       | 2 ETH | balances[Alice] = 2 ETH |
| Bob   | deposit()       | 1 ETH | balances[Bob] = 1 ETH   |
| Alice | withdraw(1 ETH) | —     | balances[Alice] = 1 ETH |

Contract holds 3 ETH total in balance (`address(this).balance`).

---

## 🔁 EXPECTED CHANGES THEY MIGHT ASK

1. **Add function to view total bank balance**

   ```solidity
   function getContractBalance() public view returns (uint256) {
       return address(this).balance;
   }
   ```

2. **Add onlyOwner withdrawal (admin feature)**

   ```solidity
   address public owner = msg.sender;
   modifier onlyOwner() { require(msg.sender == owner, "Not owner"); _; }
   ```

3. **Handle reentrancy using ReentrancyGuard (OpenZeppelin)**

   ```solidity
   import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
   contract Bank is ReentrancyGuard {
       function withdraw(uint amount) public nonReentrant { ... }
   }
   ```

4. **Add a fallback/receive function**

   ```solidity
   receive() external payable {
       deposit();
   }
   ```

5. **Add transfer between users**

   ```solidity
   function transferFunds(address to, uint amount) public {
       require(balances[msg.sender] >= amount, "Insufficient balance");
       balances[msg.sender] -= amount;
       balances[to] += amount;
   }
   ```

6. **Show gas optimization using unchecked blocks**

   ```solidity
   unchecked { balances[msg.sender] -= amount; }
   ```

---

## 🎓 VIVA QUESTIONS

**Q1. What is the purpose of `payable` in Solidity?**
It allows the function to receive Ether.

**Q2. Difference between `msg.value` and `address(this).balance`?**

* `msg.value`: Ether sent in current transaction.
* `address(this).balance`: Total Ether stored in the contract.

**Q3. Why use `require()`?**
For validation — it reverts the transaction if condition fails, refunding gas for unused execution.

**Q4. What is an event used for?**
To log data on-chain for off-chain reading (e.g., by dapps or block explorers).

**Q5. What security pattern is followed in withdraw()?**
**Checks-Effects-Interactions** — prevents reentrancy attacks.

**Q6. What happens if `.transfer()` fails?**
It reverts automatically and refunds gas.

**Q7. How can you prevent reentrancy?**
By updating state before sending Ether, using ReentrancyGuard, or using `.call()` carefully.

---

## ⚙️ TESTING & DEPLOYMENT CHEATSHEET

**Compile & Deploy:**

```bash
forge create Bank --rpc-url <RPC_URL> --private-key <KEY>
```

or in Remix:

1. Deploy contract.
2. Call `deposit()` with Ether value (e.g., 1 ether).
3. Use `getBalance()` to check.
4. Call `withdraw(amount)` to retrieve.

**Test on Sepolia (Hardhat or Foundry):**

```bash
npx hardhat test
```

Simulate deposits and withdrawals in test cases.

---

## 🧠 INSIGHT TO REMEMBER

This simple Bank contract demonstrates **Ethereum’s fundamental idea**:

> Trust in code, not intermediaries.

Even though it’s minimal, it embodies key blockchain principles:

* **Transparency** (events log everything)
* **Immutability** (once deployed)
* **Security-first design** (require checks, no arbitrary access)

Once you master this, you’re only one layer away from writing DeFi vaults, escrow contracts, and staking protocols.

---

Would you like me to extend this with **security analysis** (covering reentrancy, overflow, and gas refund tricks) and a **frontend integration snippet using Ethers.js** — the same way you’d build a simple DApp dashboard for this Bank?