

const axios = require("axios");







axios.get('http://127.0.0.1:8008/movie/?limit=10&offset=0&type=10movies?type=1&page=1').then(ret => {
	
	console.log(ret)

	const {data} = ret;
	console.log(data)
	
});




