value = "value"
left = "left"
right = "right"

tree1 = {
    value: 20,
    right: {
        value: 50,
        right: {
            value: 100,
            right: None,
            left: None,
        },
        left: {
            value: 30,
            right: {
                value: 45,
                right: None,
                left: None,
            },
            left: {
                value: 29,
                right: None,
                left: None,
            },
        },
    },
    left: {
        value: 10,
        right: {
            value: 15,
            right: None,
            left: None,
        },
        left: {
            value: 5,
            right: {
                value: 7,
                right: None,
                left: None,
            },
            left: None,
        },
    },
}

tree2 = {
    value: 20,
    right: {
        value: 50,
        right: None,
        left: {
            value: 30,
            right: {
                value: 45,
                right: {
                    value: 49,
                    left: None,
                    right: None,
                },
                left: None,
            },
            left: {
                value: 29,
                right: None,
                left: {
                    value: 21,
                    right: None,
                    left: None,
                },
            },
        },
    },
    left: {
        value: 10,
        right: {
            value: 15,
            right: None,
            left: None,
        },
        left: {
            value: 5,
            right: {
                value: 7,
                right: None,
                left: None,
            },
            left: None,
        },
    },
}
