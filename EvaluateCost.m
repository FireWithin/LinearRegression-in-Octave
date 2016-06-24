function j = EvaluateCost(x, y, theta)
	predictions = x * theta;
	square_error = (predictions - y) .^2;
	m = size(x,1);
	j =sum((square_error))/(2*m);

