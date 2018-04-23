# Scorum tests
Python behave tests for Scorum JSON RPC

#Tests CI status
[![build status](https://circleci.com/gh/KorolevskyMax/scorum-tests.svg?style=shield&circle-token=5bbec092398d9c73a76d7861e019fda4989c4ebd)](https://circleci.com/gh/KorolevskyMax/scorum-tests.svg?style=shield&circle-token=5bbec092398d9c73a76d7861e019fda4989c4ebd)

#Howto start tests:
```
To start tests you should execute:
    pip install -r "requirements.txt
and then:
    behave
or execute:
    docker-compose build
    docker-compose up
```
#Task description:

Blockchain is a continuously growing list of records, called blocks, which are linked.
Scorum blockchain generate new block every 3 second. With provided API you could get block information.

```
curl --data-binary '{"method": "call", "id": 0, "params": ["database_api", "get_block", [1]], "jsonrpc": "2.0"}' -H 'content-type:text/plain;' https://rpc.scorum.com
{
  "id": 0,
  "result": {
    "previous": "0000000000000000000000000000000000000000",
    "timestamp": "2018-01-30T12:23:36",
    "witness": "initdelegate",
    "transaction_merkle_root": "0000000000000000000000000000000000000000",
    "extensions": [
      [
        1,
        "0.0.1"
      ]
    ],
    "witness_signature": "1f0989b0d65cbe940b0e67af8e975483d452003de8c52c62a77ab6ead638dc209c47d20baa2b5f736b3a146801b544de525c48fcee3b45cb7d9b52a24c6d268c9f",
    "transactions": [],
    "block_id": "0000000152b87d7f7e7a58385eadfec018e3a647",
    "signing_key": "SCR6CQwBYjQLYJnmw5HG8Z2cDoQQzf9MQrEu6X67XszkXXN3foZap",
    "transaction_ids": []
  }
}

curl --data-binary '{"method": "call", "id": 0, "params": ["database_api", "get_dynamic_global_properties", []], "jsonrpc": "2.0"}' -H 'content-type:text/plain;' https://rpc.scorum.com
{
  "id": 0,
  "result": {
    "id": 0,
    "head_block_number": 434538,
    "head_block_id": "0006a16a68f9499032fc89bee659a0b5e49e41a4",
    "time": "2018-02-14T14:33:54",
    "current_witness": "user20",
    "total_supply": "15000100.000 SCR",
    "accounts_current_supply": "5197088.319 SCR",
    "confidential_supply": "0.000 SCR",
    "total_vesting_fund_scorum": "54780.690 SCR",
    "total_vesting_shares": "39.165548 SP",
    "total_reward_shares2": "0",
    "maximum_block_size": 131072,
    "current_aslot": 548678,
    "recent_slots_filled": "340282366920938463463374607431768211455",
    "participation_count": 128,
    "last_irreversible_block_num": 434517,
    "vote_power_reserve_rate": 40,
    "invite_quorum": 60,
    "dropout_quorum": 60,
    "change_quorum": 60,
    "current_reserve_ratio": 200000000,
    "average_block_size": 117,
    "max_virtual_bandwidth": "528482304000000000000"
  }
}
```

# Task
You have group of nodes ["node1.scorum.com", "node2.scorum.com", "node3.scorum.com"] which are synced by p2p protocol. This nodes have same API described above. 
You need create test or group of tests which should check blocks production, using python.
Please send your solution as python file. Or as a link to GitHub repo.
