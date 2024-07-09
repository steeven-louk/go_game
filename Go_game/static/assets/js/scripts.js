 let board = new WGo.Board(document.getElementById("board-container"), {
        width: 400
    });
    board.addEventListener("click", function(x, y) {
        board.addObject({
            x: x,
            y: y,
            c: board.turn
        });
        board.turn = -board.turn;
    });