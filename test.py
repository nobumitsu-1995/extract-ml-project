from CONST import TEST_DATA
from extract import extract_to_json

LABELS = ["TITLE", "SUMMARY", "PRICE"]


def run_tests():
    total = len(TEST_DATA)
    label_correct = {label: 0 for label in LABELS}
    full_correct = 0
    failures = []

    print(f"テスト開始（{total}件）...\n")

    for i, case in enumerate(TEST_DATA, 1):
        text = case["text"]
        expected = case["expected"]
        predicted = extract_to_json(text)

        case_result = {}
        all_match = True
        for label in LABELS:
            pred_val = predicted.get(label, "")
            exp_val = expected.get(label, "")
            matched = pred_val == exp_val
            if matched:
                label_correct[label] += 1
            else:
                all_match = False
            case_result[label] = (matched, pred_val, exp_val)

        if all_match:
            full_correct += 1
            print(f"[{i:2}/{total}] ✓ {text}")
        else:
            failures.append((i, text, case_result))
            print(f"[{i:2}/{total}] ✗ {text}")

    print("\n" + "=" * 50)
    print("採点結果")
    print("=" * 50)
    print(f"完全一致: {full_correct}/{total}  ({full_correct/total*100:.1f}%)")
    print("\nラベル別正解率:")
    for label in LABELS:
        count = label_correct[label]
        print(f"  {label:8}: {count}/{total}  ({count/total*100:.1f}%)")

    if failures:
        print("\n" + "=" * 50)
        print(f"不正解の詳細（{len(failures)}件）")
        print("=" * 50)
        for i, text, result in failures:
            print(f"\n[#{i}] {text}")
            for label in LABELS:
                matched, pred, exp = result[label]
                mark = "✓" if matched else "✗"
                print(f"  {mark} {label:8} 予測: '{pred}'  /  正解: '{exp}'")


if __name__ == "__main__":
    run_tests()
