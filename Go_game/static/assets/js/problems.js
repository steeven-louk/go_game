document.addEventListener("DOMContentLoaded", function() {
    const board = new WGo.Board(document.getElementById("problem-board"), {
        width: 300
    });
    const black_positions = JSON.parse(document.getElementById("black-positions").textContent);
    const white_positions = JSON.parse(document.getElementById("white-positions").textContent);
    const solution_positions = JSON.parse(document.getElementById('solution-positions').textContent);

    for (let pos of black_positions) {
        board.addObject({
            x: pos[0],
            y: pos[1],
            c: WGo.B
        });
    }
    for (let pos of white_positions) {
        board.addObject({
            x: pos[0],
            y: pos[1],
            c: WGo.W
        });
    }

    const solutionBtn = document.getElementById('solutionBtn ');
    solutionBtn.onclick = function() {
        for (let pos of solution_positions) {
            board.addObject({
                x: pos[0],
                y: pos[1],
                c: solution_positions.move === 'B' ? WGo.B : WGo.W
            });
        }
    };
});
