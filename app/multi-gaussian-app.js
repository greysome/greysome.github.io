var board, focus1, focus2, point, ellipse, all_objs;

document.getElementById("btn_submit").onclick = function() {
    // Covariance matrix elements
    var a = parseFloat(document.getElementById("input_a").value);
    var b = parseFloat(document.getElementById("input_b").value);
    var c = parseFloat(document.getElementById("input_c").value);

    // Eigenvalues
    var sq = Math.sqrt((a-c)*(a-c) + 4*b*b);
    var ev1 = ((a+c) + sq) / 2;
    var ev2 = ((a+c) - sq) / 2;

    if (ev1 <= 0 || ev2 <= 0) {
	alert("Covariance matrix not positive definite!");
	return;
    }

    // Major/minor axes of ellipse
    var axis1 = 2 * Math.sqrt(ev1);
    var axis2 = 2 * Math.sqrt(ev2);

    // Orthonormal basis of eigenvectors
    var v1, v1_dist;
    if (b == 0) {
	v1 = [1, 0];
	v1_dist = 1;
    }
    else {
	v1 = [1, (ev1-a)/b];
	v1_dist = 1 + Math.pow((ev1-a)/b, 2);
    }
    // Normalise
    v1 = [v1[0]/v1_dist, v1[1]/v1_dist];

    // Draw stuff
    var C = Math.sqrt(Math.abs(axis1*axis1 - axis2*axis2)); // Focus to center
    board.removeObject(all_objs);

    all_objs = [];
    console.log(jStat.chisquare.inv(0.01, 2));
    console.log(jStat.chisquare.inv(0.05, 2));
    console.log(jStat.chisquare.inv(0.1, 2));
    for (var p = 0; p < 0.8; p += 0.1) {
	// Construct each confidence region
	var maha_dist = Math.sqrt(jStat.chisquare.inv(p, 2));
	var v1_ = [v1[0]/maha_dist, v1[1]/maha_dist];

	focus1 = board.create('point', [v1_[0]*C, v1_[1]*C]);
	focus2 = board.create('point', [-v1_[0]*C, -v1_[1]*C]);
	point = board.create('point', [v1_[0]*axis1, v1_[1]*axis1]);
	focus1.hideElement();
	focus2.hideElement();
	point.hideElement();
	ellipse = board.create('ellipse', [focus1, focus2, point]);
	all_objs.push([focus1, focus2, point, ellipse]);
    }
}

board = JXG.JSXGraph.initBoard('jxgbox', { 
    boundingbox: [-5.0, 5.0, 5.0, -5.0],
    axis: true,
    showCopyright: false,
    showNavigation: true
});
