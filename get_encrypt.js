var CryptoJS = require('crypto-js');

function encrypt_(angle, as, backstr) {
    var tt = {
        "cl": [
            {
                "x": 862,
                "y": 287,
                "t": 1657760616916
            }
        ],
        "mv": [
            {
                "fx": 987,
                "fy": 149,
                "t": 1657760613905,
                "bf": 2
            },
            {
                "fx": 979,
                "fy": 370,
                "t": 1657760615529,
                "bf": 2
            },
            {
                "fx": 948,
                "fy": 339,
                "t": 1657760615688,
                "bf": 2
            },
            {
                "fx": 911,
                "fy": 321,
                "t": 1657760615848,
                "bf": 2
            },
            {
                "fx": 892,
                "fy": 309,
                "t": 1657760616008,
                "bf": 2
            },
            {
                "fx": 880,
                "fy": 299,
                "t": 1657760616176,
                "bf": 2
            },
            {
                "fx": 869,
                "fy": 290,
                "t": 1657760616440,
                "bf": 2
            },
            {
                "fx": 864,
                "fy": 288,
                "t": 1657760616641,
                "bf": 2
            },
            {
                "fx": 862,
                "fy": 287,
                "t": 1657760616866,
                "bf": 2
            },
            {
                "fx": 864,
                "fy": 288,
                "t": 1657760617026,
                "bf": 1
            },
            {
                "fx": 877,
                "fy": 293,
                "t": 1657760617186,
                "bf": 1
            },
            {
                "fx": 882,
                "fy": 295,
                "t": 1657760617360,
                "bf": 1
            },
            {
                "fx": 891,
                "fy": 298,
                "t": 1657760617537,
                "bf": 1
            },
            {
                "fx": 900,
                "fy": 300,
                "t": 1657760617688,
                "bf": 1
            },
            {
                "fx": 908,
                "fy": 301,
                "t": 1657760617864,
                "bf": 1
            },
            {
                "fx": 910,
                "fy": 301,
                "t": 1657760618585,
                "bf": 1
            }
        ],
        "sc": [],
        "kb": [
            {
                "key": "a",
                "t": 1657760606047
            }
        ],
        "sb": [],
        "sd": [],
        "sm": [],
        "cr": {
            "screenTop": 0,
            "screenLeft": 0,
            "clientWidth": 1920,
            "clientHeight": 979,
            "screenWidth": 1920,
            "screenHeight": 1080,
            "availWidth": 1920,
            "availHeight": 1050,
            "outerWidth": 1920,
            "outerHeight": 1050,
            "scrollWidth": 1920,
            "scrollHeight": 1920
        },
        "simu": 0,
        "ac_c": (angle * 212 / 360 / 212).toFixed(2),
        "backstr": backstr
    };
    var t = as + 'appsapi0'
        , n = CryptoJS.enc.Utf8.parse(t)
        , i = CryptoJS.enc.Utf8.parse(JSON.stringify(tt))
        , r = CryptoJS.AES.encrypt(i, n, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    });
    return [r.toString(), tt['ac_c']];
}

function add(x,y) {
    return x+y;
}

//console.log(encrypt_('175','77af72b4','3665-Px4DcLoit3uVe824uBkHUhYlQRP9J1snLUo3oUo4NCni3QAeNyHrm3CQYE1d0+bG4z2Vv/PQXdv1Qp9j+bImhNo+yvQeYZjOGBVq/fJYQARPO+z357jr0N2VdtJR6PLV/ZF/4vWSekHq0V0F9PvNX4E9FL+bBVTtveoWXlDB3zxsr30wdtMey7lw/HDDDKm05KTU72MoN+B2g6pXkXJLfwXeK557yhbIgeqaUUxYRgI46RjrwoF1Em3LISq+4Ke5TIyH89awQ6ups+DSlxyJZbU/WxmL6wSrpxmVpQ0rYrwgtgO8yAPCE2myWZ7uQnMkWTnNNBThHZHALC3YA4xWkA=='))
