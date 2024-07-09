 let board = new WGo.Board(document.getElementById("board-container"), {
        width: 400
    });
    console.log("board, board", board)
    // Example code for WGo
    board.addEventListener("click", function(x, y) {
        board.addObject({
            x: x,
            y: y,
            c: board.turn
        });
        board.turn = -board.turn;
    });


//PROBLEME SCRIPT
/*document.addEventListener("DOMContentLoaded", function() {
    var board = new WGo.Board(document.getElementById("problem-board"), {
        width: 100
    });
    var black_positions = JSON.parse(document.getElementById("black-positions").textContent);
    var white_positions = JSON.parse(document.getElementById("white-positions").textContent);

    for (var pos of black_positions) {
        board.addObject({
            x: pos[0],
            y: pos[1],
            c: WGo.B
        });
    }
    for (var pos of white_positions) {
        board.addObject({
            x: pos[0],
            y: pos[1],
            c: WGo.W
        });
    }
});
*/
 // static/js/problem_board.js
document.addEventListener("DOMContentLoaded", function() {
    var board = new WGo.Board(document.getElementById("problem-board"), {
        width: 400
    });

    var problemData = JSON.parse(document.getElementById("problem-data").textContent);

    // Positions des pierres noires (AB) et blanches (AW)
    var black_positions = problemData.AB.map(pos => [pos.charCodeAt(0) - 97, pos.charCodeAt(1) - 97]);
    var white_positions = problemData.AW.map(pos => [pos.charCodeAt(0) - 97, pos.charCodeAt(1) - 97]);

    // Ajouter les pierres noires
    for (var pos of black_positions) {
        board.addObject({
            x: pos[0],
            y: pos[1],
            c: WGo.B
        });
    }

    // Ajouter les pierres blanches
    for (var pos of white_positions) {
        board.addObject({
            x: pos[0],
            y: pos[1],
            c: WGo.W
        });
    }

    // Afficher la description du problème (C)
    if (problemData.C) {
        var descriptionElement = document.createElement('p');
        descriptionElement.textContent = problemData.C;
        document.body.appendChild(descriptionElement);
    }
});
