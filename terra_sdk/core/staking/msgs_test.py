from terra_sdk.core.staking import MsgDelegate, MsgUndelegate, MsgBeginRedelegate


def test_deserialize_msg_delegate_examples(load_msg_examples):
    examples = load_msg_examples(MsgDelegate.type, __file__, "./MsgDelegate.data.json")
    for example in examples:
        assert MsgDelegate.from_data(example).to_data() == example


def test_deserialize_msg_undelegate_examples(load_msg_examples):
    examples = load_msg_examples(
        MsgUndelegate.type, __file__, "./MsgUndelegate.data.json"
    )
    for example in examples:
        assert MsgUndelegate.from_data(example).to_data() == example


def test_deserialize_msg_begin_redelegate_examples(load_msg_examples):
    examples = load_msg_examples(
        MsgBeginRedelegate.type, __file__, "./MsgBeginRedelegate.data.json"
    )
    for example in examples:
        assert MsgBeginRedelegate.from_data(example).to_data() == example