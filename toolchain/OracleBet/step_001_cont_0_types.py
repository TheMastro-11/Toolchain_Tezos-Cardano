import smartpy as sp

tstorage = sp.record(deadline = sp.nat, oracle = sp.option(sp.address), player1 = sp.option(sp.address), player1Deposit = sp.bool, player2 = sp.option(sp.address), player2Deposit = sp.bool, winner = sp.option(sp.address)).layout(("deadline", ("oracle", ("player1", ("player1Deposit", ("player2", ("player2Deposit", "winner")))))))
tparameter = sp.variant(deposit = sp.record(oracle = sp.address, player2 = sp.address).layout(("oracle", "player2")), deposit2 = sp.unit, election = sp.address, withdraw = sp.unit).layout((("deposit", "deposit2"), ("election", "withdraw")))
tprivates = { }
tviews = { }
