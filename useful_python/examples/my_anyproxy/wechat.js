

module.exports = {
  *beforeSendResponse(requestDetail, responseDetail) {
      if (requestDetail.url.indexOf("https://mp.weixin.qq.com/mp/getappmsgext?f=json") !== -1) {
      const newResponse = responseDetail.response;

      const body =newResponse.body;

      const json_content = JSON.parse(body)
      console.log("*************************************评论数量************************************************************************************************************************************************************************************:"+body);

      return null;
    }
  },



};