const request = require('request-promise');

exports.runner = (req, res) => {
    const receivingServiceURL = process.env.API_URI;
    const metadataServerTokenURL = 'http://metadata/computeMetadata/v1/instance/service-accounts/default/identity?audience=';
    const tokenRequestOptions = {
        uri: metadataServerTokenURL + receivingServiceURL,
        headers: {
            'Metadata-Flavor': 'Google'
        }
    };

    request(tokenRequestOptions)
    .then((token) => {
        return request({
            method: 'POST',
            uri: receivingServiceURL,
            body: req.body
        }).auth(null, null, true, token)
    })
    .then((response) => {
        res.status(200).send(response);
    })
    .catch((error) => {
        res.status(400).send(error);
    });  
};
