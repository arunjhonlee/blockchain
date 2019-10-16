from web3 import Web3
import json

gananche_url='http://127.0.0.1:7545'
web3 =Web3(Web3.HTTPProvider(gananche_url))

abi=json.loads('[{"constant":true,"inputs":[],"name":"readMessage","outputs":[{"name":"","type":"string"},{"name":"","type":"uint256"},{"name":"","type":"uint256"},{"name":"","type":"uint256"},{"name":"","type":"uint256"},{"name":"","type":"string"},{"name":"","type":"bool"},{"name":"","type":"bool"},{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_bank","type":"address"}],"name":"dealer2","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_qwer","type":"address"}],"name":"check1","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"dealerread","outputs":[{"name":"","type":"string"},{"name":"","type":"uint256"},{"name":"","type":"uint256"},{"name":"","type":"uint256"},{"name":"","type":"uint256"},{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_asd","type":"address"}],"name":"check","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_recipient","type":"address"},{"name":"_name","type":"string"},{"name":"_age","type":"uint256"},{"name":"_adharnumber","type":"uint256"},{"name":"_accountnumber","type":"uint256"},{"name":"_salary","type":"uint256"},{"name":"_location","type":"string"},{"name":"_license","type":"uint256"}],"name":"sendMessage","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_zxc","type":"address"}],"name":"department","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_verification","type":"address"}],"name":"dealer1","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_vbn","type":"address"}],"name":"department1","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]');
address='0x7Ccd41911465909A204b355CD663A84Edc2fCb76'
contract=web3.eth.contract(address=address,abi=abi)

def Transaction(account1,account2,amount,private_key):
    nonce = web3.eth.getTransactionCount(account2)
    tx ={
        'nonce' :nonce,
        'to': account1,
        'value': web3.toWei(amount,'ether'),
        'gas':2000000,
        'gasPrice':web3.toWei('50','gwei'),

    }
    signed_tx = web3.eth.account.signTransaction(tx,private_key)
    tx_hash=web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return (web3.toHex(tx_hash))


web3.eth.defaultAccount=web3.eth.accounts[0]
name=input('enter your name = ')
age=int(input('enter the age = '))
adharnumber=int(input('enter the adharnumber = '))
accountnumber=int(input('enter the accountnumber = '))
salary=int(input('enter the salary = '))
location=input('enter your location = ')
license=int(input('enter the license = '))
contract.functions.sendMessage(web3.eth.accounts[1],name,age,adharnumber,accountnumber,salary,location,license).transact()
web3.eth.defaultAccount=web3.eth.accounts[1]
a=contract.functions.readMessage().call()
# print(a)
contract.functions.dealer1(web3.eth.accounts[2]).transact()
web3.eth.defaultAccount=web3.eth.accounts[2]
b=contract.functions.dealerread().call()
# print(b)
contract.functions.dealer2(web3.eth.accounts[1]).transact()
c=contract.functions.dealerread().call()
# print(c)
contract.functions.check1(web3.eth.accounts[3]).transact()
web3.eth.defaultAccount=web3.eth.accounts[1]
contract.functions.check1(web3.eth.accounts[3]).transact()
web3.eth.defaultAccount=web3.eth.accounts[3]
contract.functions.check(web3.eth.accounts[1]).transact()

web3.eth.defaultAccount=web3.eth.accounts[1]

contract.functions.department(web3.eth.accounts[4]).transact()
web3.eth.defaultAccount=web3.eth.accounts[4]
contract.functions.department1(web3.eth.accounts[1]).transact()
web3.eth.defaultAccount=web3.eth.accounts[1]
d=contract.functions.readMessage().call()
# print(d)
deler_res=d[6]
insur_res=d[7]
dep_res=d[8]
if((deler_res==True) and (insur_res==True) and (dep_res==0)):
    print('loan accepted')
    private_key='e7bc2cd3312a1f5deb33e4570c64b83212ee353b85a4f202774088a4a6452886'
    e=Transaction(web3.eth.accounts[0],web3.eth.accounts[1],1,private_key)
    print(e)
else:
    print('loan denied')
