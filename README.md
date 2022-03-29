# A Blockchain-based Electronic Voting System

### Description
This is a blockchain-inspired "Internet" voting system that demonstrates how a blockchain architecture can be used to make the voting process more reliable. It keeps track of voters that have been authenticated as well as ballots that are cast in two separate, unlinked blockchains. This preserves voter anonymity and achieves greater election integrity using an "immutable" audit trail. 

The system allows users to configure their own voter roll and ballot with multiple ballot items and multiple selections per item. It aims to simulate the decentralized nature of blockchain with a consensus process that must take place before votes are recorded on the blockchain using BFTP.

### Features
- full voting system (registration, authentication, Internet ballot interface)
- interactive (normal) mode vs. simulated election
- demonstrates consensus process among nodes in the blockchain
- adversarial mode (mocks adversary nodes and demonstrates power of consensus)
- logging (machine logs emulate realistic system messages that is part of the system's auditing)

### Requirements
Docker OR Python 3.5+ & pip

### How to Run
You can use `docker` to run this application. See [docker instructions](https://github.com/Debagnik/voting_on_Blockchain/blob/master/README.Docker.md) for more.

Alternatively, you can set up the environment using `pip` to install the dependencies from `requirements.txt` (ideally in a virtual environment).
Then run `python main.py`. To customize the software for your own voter roll & ballot, modify `configs/voter_roll.json` and `configs/ballot_config.json`, respectively.

Written by Debagnik Kar for Major Project submission to partially complete B.Tech curriculam in Electronics and telecommunication engineering from School of Electronics Engineering, Kalinga Institute of Industrial Technology, [KIIT Deemed to be University](https://electronics.kiit.ac.in/), Bhubaneswar, Odisha.