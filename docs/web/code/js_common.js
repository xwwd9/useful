const request = require('request')


async function checkProxy(proxyUrl) {
    // 检测代理是否有效
    const resp = await new Promise((resolve, reject) => {
        request.get({
            url: 'http://ip-api.com/json',
            proxy: proxyUrl,
            json: true
        }, (err, resp, body) => {
            if (err) {
                reject(err)
                return
            } else {
                resolve(body)
                return
            }
        })
    })
    if (!resp || !resp.status || resp.status !== 'success') {
        return false
    }
    return true
}


checkProxy("http://127.0.0.1:10809")

// export {checkProxy};

module.exports = {
    checkProxy
};
