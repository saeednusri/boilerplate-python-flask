const request = require('request-promise');

exports.runner = (req, res) => {
    const receivingServiceURL = 'https://boilerplate-cloud-functions-57e3askhva-uc.a.run.app';
    const metadataServerTokenURL = 'http://metadata/computeMetadata/v1/instance/service-accounts/default/identity?audience=';
    const tokenRequestOptions = {
        uri: metadataServerTokenURL + receivingServiceURL,
        headers: {
            'Metadata-Flavor': 'Google'
        }
    };

    request(tokenRequestOptions)
    .then((token) => {
        return request(receivingServiceURL).auth(null, null, true, token)
    })
    .then((response) => {
        res.status(200).send(response);
    })
    .catch((error) => {
        res.status(400).send(error);
    });  
};
