document.addEventListener("DOMContentLoaded", function() {
    var board = new WGo.Board(document.getElementById("problem-board"), {
        width: 300
    });
    var black_positions = JSON.parse(document.getElementById("black-positions").textContent);
    var white_positions = JSON.parse(document.getElementById("white-positions").textContent);
    var solution_positions = JSON.parse(document.getElementById('solution-positions').textContent);

    console.log(black_positions)
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

        var solutionBtn = document.getElementById('solutionBtn ');
    solutionBtn.onclick = function() {
        for (var pos of solution_positions) {
            board.addObject({
                x: pos[0],
                y: pos[1],
                c: solution_positions.move === 'B' ? WGo.B : WGo.W
            });
        }
    };
});
