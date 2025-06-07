def tree_depth_9(days, miles, receipts):
    # ROOT NODE: Perfectly stable root split at `receipts <= 828.10` across all analyzed depths (6, 7, 8, 9).
    # This is the undeniable "master switch" of the legacy system, as documented in the progress_summary.md.
    if receipts <= 828.10:
        # PATH: Low-to-moderate total receipts (<= $828.10).
        # The split on `days <= 4.50` is also perfectly stable, confirming trip duration as the second most important factor.
        if days <= 4.50:
            # PATH: Short trips (<= 4.5 days) with low receipts.
            # TREND: The logic in this branch is IDENTICAL to the depth-8 tree. This is a major finding.
            # It indicates that for short, low-receipt trips, the model's accuracy gains (from 10% to 20% exact matches)
            # are NOT coming from this segment. The logic here has converged and reached its optimal state at depth 8.
            # All splits and leaf values below are STABLE from depth 8.
            if miles <= 583.00:
                # PATH: Short trips, low receipts, and low-to-medium mileage (local/regional).
                if receipts <= 443.43:
                    # PATH: Very low receipts (<$443) on a short, low-mileage trip.
                    if days <= 1.50:
                        # PATH: 1-day trips.
                        if miles <= 161.00:
                            # PATH: 1-day, very low mileage trip (<161 mi).
                            if miles <= 67.50:
                                # PATH: 1-day, extremely low mileage trip (<67.5 mi).
                                if miles <= 56.50:
                                    if miles <= 51.00:
                                        return 128.91 # LEAF 1: STABLE from d8. A new leaf created at d8, fine-tuning the base reimbursement.
                                    else:  # miles > 51.00
                                        return 126.06 # LEAF 2: STABLE from d8. The value here is slightly lower, suggesting a tiny penalty. This deep nesting to model a tiny difference is a classic contortion.
                                else:  # miles > 56.50
                                    if receipts <= 7.09:
                                        return 117.24 # LEAF 3: STABLE from d8. CONTORTION: A new penalty pocket for trips with almost no receipts (<$7.09), confirming Kevin's "tiny receipt penalty" theory.
                                    else:  # receipts > 7.09
                                        return 120.65 # LEAF 4: STABLE from d8. The "normal" value for this path, which is still lower than the reimbursement for <51 miles.
                            else:  # miles > 67.50
                                # PATH: 1-day, 67.5-161 mi trip.
                                if receipts <= 172.91:
                                    if miles <= 136.50:
                                        return 170.98 # LEAF 5: STABLE from d8. D8 refined this from d7 by adding the mileage split, creating two tiers of bonus.
                                    else:  # miles > 136.50
                                        return 197.41 # LEAF 6: STABLE from d8. Higher mileage bonus tier.
                                else:  # receipts > 172.91
                                    return 150.34 # LEAF 7: STABLE from d8. The consistent penalty for having slightly higher receipts.
                        else:  # miles > 161.00
                            # PATH: 1-day, higher mileage (161-583 mi).
                            if miles <= 499.50:
                                # PATH: 1-day, 161-499.5 mi.
                                if receipts <= 290.99:
                                    if receipts <= 143.65:
                                        return 225.12 # LEAF 8: STABLE from d8. D8 split d7's logic here to create a new receipt tier.
                                    else:  # receipts > 143.65
                                        return 293.53 # LEAF 9: STABLE from d8. Higher receipt tier bonus.
                                else:  # receipts > 290.99
                                    if miles <= 365.00:
                                        return 198.42 # LEAF 10: STABLE from d8. Penalty pocket.
                                    else:  # miles > 365.00
                                        return 221.23 # LEAF 11: STABLE from d8. Slightly lower penalty.
                            else:  # miles > 499.50
                                return 355.57 # LEAF 12: STABLE from d6, d7, d8. A hard-coded cap.
                    else:  # days > 1.50
                        # PATH: 2-4 day, low-mileage trips.
                        if miles <= 188.50:
                            # PATH: Very low mileage over 2-4 days.
                            if days <= 2.50:
                                # PATH: 2-day trips.
                                if miles <= 118.00:
                                    if miles <= 55.00:
                                        return 204.05 # LEAF 13: STABLE from d8. D8 added this mileage split to refine the low-efficiency penalty.
                                    else:  # miles > 55.00
                                        return 234.20 # LEAF 14: STABLE from d8. Slightly lower penalty.
                                else:  # miles > 118.00
                                    return 325.56 # LEAF 15: STABLE from d7, d8.
                            else:  # days > 2.50
                                # PATH: 3-4 day trips.
                                if miles <= 140.50:
                                    if receipts <= 291.27:
                                        return 376.56 # LEAF 16: STABLE from d8.
                                    else:  # receipts > 291.27
                                        return 303.20 # LEAF 17: STABLE from d8. Penalty pocket.
                                else:  # miles > 140.50
                                    if miles <= 164.50:
                                        return 406.91 # LEAF 18: STABLE from d8.
                                    else:  # miles > 164.50
                                        return 431.01 # LEAF 19: STABLE from d8.
                        else:  # miles > 188.50
                            # PATH: Moderate mileage (188-583 mi) over 2-4 days.
                            if receipts <= 312.49:
                                # PATH: Very low receipts (<$312).
                                if days <= 3.50:
                                    if receipts <= 60.82:
                                        return 494.63 # LEAF 20: STABLE from d8. D8 added this receipt tier, likely to model Kevin's "tiny receipt penalty".
                                    else:  # receipts > 60.82
                                        return 541.76 # LEAF 21: STABLE from d8. "Normal" value.
                                else:  # days > 3.50
                                    if miles <= 391.00:
                                        return 664.43 # LEAF 22: STABLE from d8.
                                    else:  # miles > 391.00
                                        return 631.50 # LEAF 23: STABLE from d8. Mileage penalty.
                            else:  # receipts > 312.49
                                if miles <= 394.50:
                                    return 406.36 # LEAF 24: STABLE from d8. Penalty pocket.
                                else:  # miles > 394.50
                                    return 415.96 # LEAF 25: STABLE from d8. Slightly less severe penalty.
                else:  # receipts > 443.43
                    # PATH: "Moderate" receipts ($443-$828) on a short, low-mileage trip.
                    if receipts <= 639.15:
                        # PATH: Receipts between $443 and $639.
                        if days <= 1.50:
                            # PATH: 1-day trip with moderate receipts.
                            if miles <= 499.00:
                                if miles <= 441.50:
                                    if receipts <= 512.79:
                                        return 362.34 # LEAF 26: STABLE from d8.
                                    else:  # receipts > 512.79
                                        return 425.57 # LEAF 27: STABLE from d8.
                                else:  # miles > 441.50
                                    return 162.18 # LEAF 28: STABLE from d8. Severe penalty pocket.
                            else:  # miles > 499.00
                                return 616.27 # LEAF 29: STABLE from d7, d8.
                        else:  # days > 1.50
                            # PATH: 2-4 day trip with moderate receipts.
                            if miles <= 327.50:
                                if receipts <= 530.64:
                                    if miles <= 151.00:
                                        return 458.35 # LEAF 30: STABLE from d8.
                                    else:  # miles > 151.00
                                        return 437.40 # LEAF 31: STABLE from d8. Penalty pocket.
                                else:  # receipts > 530.64
                                    if days <= 3.50:
                                        return 568.44 # LEAF 32: STABLE from d8.
                                    else:  # days > 3.50
                                        return 682.22 # LEAF 33: STABLE from d8.
                            else:  # miles > 327.50
                                if miles <= 450.50:
                                    return 764.24 # LEAF 34: STABLE from d8.
                                else:  # miles > 450.50
                                    return 667.85 # LEAF 35: STABLE from d8. Mileage drop-off.
                    else:  # receipts > 639.15
                        # PATH: Higher-end of "moderate" receipts ($639-$828).
                        if receipts <= 697.81:
                            return 788.53 # LEAF 36: STABLE from d6, d7, d8. Hard-coded rule for optimal spending.
                        else:  # receipts > 697.81
                            if receipts <= 786.06:
                                if days <= 1.50:
                                    if miles <= 313.59:
                                        return 636.19 # LEAF 37: STABLE from d8.
                                    else:  # miles > 313.59
                                        return 636.51 # LEAF 38: STABLE from d8.
                                else:  # days > 1.50
                                    return 648.53 # LEAF 39: STABLE from d8.
                            else:  # receipts > 786.06
                                if miles <= 366.28:
                                    return 707.88 # LEAF 40: STABLE from d8.
                                else:  # miles > 366.28
                                    return 741.46 # LEAF 41: STABLE from d8.
            else:  # miles > 583.00
                # PATH: Short trips (<= 4.5 days) with low receipts but high mileage (high-efficiency trips).
                if receipts <= 564.47:
                    if days <= 2.50:
                        if days <= 1.50:
                            if receipts <= 444.12:
                                if miles <= 854.00:
                                    if receipts <= 228.55:
                                        return 541.27 # LEAF 42: STABLE from d8.
                                    else:  # receipts > 228.55
                                        return 500.92 # LEAF 43: STABLE from d8.
                                else:  # miles > 854.00
                                    if miles <= 992.50:
                                        return 570.71 # LEAF 44: STABLE from d8.
                                    else:  # miles > 992.50
                                        return 589.11 # LEAF 45: STABLE from d8.
                            else:  # receipts > 444.12
                                if receipts <= 499.69:
                                    return 644.12 # LEAF 46: STABLE from d8.
                                else:  # receipts > 499.69
                                    return 658.14 # LEAF 47: STABLE from d8.
                        else:  # days > 1.50
                            if miles <= 746.00:
                                if receipts <= 316.39:
                                    return 624.78 # LEAF 48: STABLE from d8.
                                else:  # receipts > 316.39
                                    return 625.15 # LEAF 49: STABLE from d8.
                            else:  # miles > 746.00
                                if receipts <= 496.85:
                                    if miles <= 934.00:
                                        return 654.10 # LEAF 50: STABLE from d8.
                                    else:  # miles > 934.00
                                        return 720.66 # LEAF 51: STABLE from d8.
                                else:  # receipts > 496.85
                                    return 752.69 # LEAF 52: STABLE from d8.
                    else:  # days > 2.50
                        if receipts <= 168.92:
                            if days <= 3.50:
                                return 711.07 # LEAF 53: STABLE from d7, d8.
                            else:  # days > 3.50
                                return 667.98 # LEAF 54: STABLE from d7, d8.
                        else:  # receipts > 168.92
                            if receipts <= 175.66:
                                return 875.39 # LEAF 55: STABLE from d7, d8. Jackpot pocket quirk.
                            else:  # receipts > 175.66
                                if miles <= 1085.00:
                                    if miles <= 1054.58:
                                        return 785.97 # LEAF 56: STABLE from d8.
                                    else:  # miles > 1054.58
                                        return 664.69 # LEAF 57: STABLE from d8.
                                else:  # miles > 1085.00
                                    if days <= 3.50:
                                        return 794.28 # LEAF 58: STABLE from d8.
                                    else:  # days > 3.50
                                        return 860.32 # LEAF 59: STABLE from d8.
                else:  # receipts > 564.47
                    if miles <= 681.50:
                        return 676.38 # LEAF 60: STABLE from d6, d7, d8. Hard-coded penalty.
                    else:  # miles > 681.50
                        if receipts <= 705.37:
                            if days <= 3.50:
                                if receipts <= 601.81:
                                    return 992.40 # LEAF 61: STABLE from d8.
                                else:  # receipts > 601.81
                                    if miles <= 948.56:
                                        return 960.47 # LEAF 62: STABLE from d8.
                                    else:  # miles > 948.56
                                        return 962.14 # LEAF 63: STABLE from d8.
                            else:  # days > 3.50
                                return 1097.95 # LEAF 64: STABLE from d7, d8.
                        else:  # receipts > 705.37
                            if miles <= 1088.00:
                                if days <= 2.50:
                                    return 1048.28 # LEAF 65: STABLE from d7, d8.
                                else:  # days > 2.50
                                    if miles <= 886.00:
                                        return 1166.93 # LEAF 66: STABLE from d8.
                                    else:  # miles > 886.00
                                        return 1116.31 # LEAF 67: STABLE from d8.
                            else:  # miles > 1088.00
                                return 1237.62 # LEAF 68: STABLE from d7, d8. Short-trip jackpot.
        else:  # days > 4.50
            # PATH: Longer trips (5+ days) with low-to-moderate receipts (<= $828.10).
            # TREND: This branch is also IDENTICAL to the depth-8 tree.
            # This is further evidence that the model has reached a point of convergence for the entire
            # low-receipts (`<= $828.10`) calculation path. The additional depth of the d9 tree is not being used here.
            # The ~10% jump in exact matches must be coming from the high-receipts branch.
            if miles <= 617.50:
                # PATH: Longer trips, low receipts, low mileage ("conference travel"). All leaves are STABLE from d8.
                if days <= 8.50:
                    # PATH: 5-8 day trips with low mileage.
                    if miles <= 258.43:
                        # PATH: Very low mileage (low efficiency).
                        if receipts <= 340.34:
                            if miles <= 114.50:
                                if receipts <= 298.69:
                                    if days <= 5.50:
                                        return 435.69 # LEAF 69: STABLE from d8.
                                    else:  # days > 5.50
                                        return 516.26 # LEAF 70: STABLE from d8.
                                else:  # receipts > 298.69
                                    if receipts <= 324.46:
                                        return 593.83 # LEAF 71: STABLE from d8.
                                    else:  # receipts > 324.46
                                        return 573.58 # LEAF 72: STABLE from d8. Penalty pocket.
                            else:  # miles > 114.50
                                if days <= 6.00:
                                    if receipts <= 320.29:
                                        return 580.01 # LEAF 73: STABLE from d8.
                                    else:  # receipts > 320.29
                                        return 538.36 # LEAF 74: STABLE from d8. Penalty pocket.
                                else:  # days > 6.00
                                    if miles <= 159.50:
                                        return 616.24 # LEAF 75: STABLE from d8.
                                    else:  # miles > 159.50
                                        return 684.66 # LEAF 76: STABLE from d8.
                        else:  # receipts > 340.34
                            if receipts <= 709.78:
                                if receipts <= 585.80:
                                    if miles <= 146.50:
                                        return 647.04 # LEAF 77: STABLE from d8.
                                    else:  # miles > 146.50
                                        return 707.25 # LEAF 78: STABLE from d8.
                                else:  # receipts > 585.80
                                    if miles <= 174.26:
                                        return 848.30 # LEAF 79: STABLE from d8.
                                    else:  # miles > 174.26
                                        return 1031.34 # LEAF 80: STABLE from d8.
                            else:  # receipts > 709.78
                                if receipts <= 764.74:
                                    return 483.34 # LEAF 81: STABLE from d7, d8. Penalty pocket.
                                else:  # receipts > 764.74
                                    return 628.40 # LEAF 82: STABLE from d7, d8. Penalty reversal.
                    else:  # miles > 258.43
                        # PATH: Moderate mileage (258-617 mi) on a 5-8 day trip.
                        if receipts <= 302.93:
                            if receipts <= 200.70:
                                if miles <= 445.50:
                                    if receipts <= 87.71:
                                        return 703.45 # LEAF 83: STABLE from d8. Tiny receipt penalty.
                                    else:  # receipts > 87.71
                                        return 686.54 # LEAF 84: STABLE from d8.
                                else:  # miles > 445.50
                                    return 718.30 # LEAF 85: STABLE from d7, d8.
                            else:  # receipts > 200.70
                                if days <= 7.50:
                                    if receipts <= 288.30:
                                        return 791.10 # LEAF 86: STABLE from d8.
                                    else:  # receipts > 288.30
                                        return 742.25 # LEAF 87: STABLE from d8. Penalty pocket.
                                else:  # days > 7.50
                                    if miles <= 438.43:
                                        return 880.41 # LEAF 88: STABLE from d8.
                                    else:  # miles > 438.43
                                        return 841.27 # LEAF 89: STABLE from d8. Mileage penalty.
                        else:  # receipts > 302.93
                            if receipts <= 685.51:
                                if miles <= 360.50:
                                    if miles <= 324.32:
                                        return 835.08 # LEAF 90: STABLE from d8.
                                    else:  # miles > 324.32
                                        return 883.11 # LEAF 91: STABLE from d8.
                                else:  # miles > 360.50
                                    if days <= 7.00:
                                        return 901.29 # LEAF 92: STABLE from d8.
                                    else:  # days > 7.00
                                        return 953.93 # LEAF 93: STABLE from d8.
                            else:  # receipts > 685.51
                                if miles <= 357.50:
                                    return 1077.35 # LEAF 94: STABLE from d8.
                                else:  # miles > 357.50
                                    return 1114.90 # LEAF 95: STABLE from d8.
                else:  # days > 8.50
                    # PATH: Very long trips (9+ days) with low mileage. All leaves are STABLE from d8.
                    if receipts <= 567.01:
                        if days <= 13.50:
                            if miles <= 92.42:
                                if days <= 9.50:
                                    return 704.94 # LEAF 96: STABLE from d8.
                                else:  # days > 9.50
                                    if miles <= 12.50:
                                        return 713.71 # LEAF 97: STABLE from d8.
                                    else:  # miles > 12.50
                                        return 796.16 # LEAF 98: STABLE from d8.
                            else:  # miles > 92.42
                                if miles <= 477.50:
                                    if days <= 10.50:
                                        return 842.03 # LEAF 99: STABLE from d8.
                                    else:  # days > 10.50
                                        return 927.22 # LEAF 100: STABLE from d8.
                                else:  # miles > 477.50
                                    if days <= 10.00:
                                        return 954.68 # LEAF 101: STABLE from d8.
                                    else:  # days > 10.00
                                        return 1152.99 # LEAF 102: STABLE from d8.
                        else:  # days > 13.50
                            if miles <= 339.50:
                                if receipts <= 272.45:
                                    return 1180.63 # LEAF 103: STABLE from d8.
                                else:  # receipts > 272.45
                                    if miles <= 182.00:
                                        return 866.76 # LEAF 104: STABLE from d8.
                                    else:  # miles > 182.00
                                        return 924.90 # LEAF 105: STABLE from d8.
                            else:  # miles > 339.50
                                if miles <= 447.50:
                                    return 1203.93 # LEAF 106: STABLE from d8.
                                else:  # miles > 447.50
                                    return 1306.64 # LEAF 107: STABLE from d8.
                    else:  # receipts > 567.01
                        if days <= 12.50:
                            if receipts <= 747.73:
                                if receipts <= 632.98:
                                    if receipts <= 617.45:
                                        return 1033.44 # LEAF 108: STABLE from d8.
                                    else:  # receipts > 617.45
                                        return 990.84 # LEAF 109: STABLE from d8.
                                else:  # receipts > 632.98
                                    if receipts <= 728.09:
                                        return 1169.26 # LEAF 110: STABLE from d8.
                                    else:  # receipts > 728.09
                                        return 1063.90 # LEAF 111: STABLE from d8.
                            else:  # receipts > 747.73
                                if receipts <= 796.73:
                                    if miles <= 401.50:
                                        return 1285.23 # LEAF 112: STABLE from d8.
                                    else:  # miles > 401.50
                                        return 1235.69 # LEAF 113: STABLE from d8.
                                else:  # receipts > 796.73
                                    return 1155.05 # LEAF 114: STABLE from d8.
                        else:  # days > 12.50
                            if miles <= 330.50:
                                if miles <= 27.50:
                                    return 1331.53 # LEAF 115: STABLE from d8.
                                else:  # miles > 27.50
                                    if days <= 13.50:
                                        return 1190.16 # LEAF 116: STABLE from d8.
                                    else:  # days > 13.50
                                        return 1295.14 # LEAF 117: STABLE from d8.
                            else:  # miles > 330.50
                                return 1516.68 # LEAF 118: STABLE from d7, d8.
            else:  # miles > 617.50
                # PATH: Longer trips (5+ days) with low receipts but high mileage. All leaves are STABLE from d8.
                if miles <= 833.50:
                    if days <= 10.50:
                        if receipts <= 500.49:
                            if days <= 6.50:
                                if receipts <= 487.86:
                                    if receipts <= 176.33:
                                        return 771.83 # LEAF 119: STABLE from d8.
                                    else:  # receipts > 176.33
                                        return 987.35 # LEAF 120: STABLE from d8.
                                else:  # receipts > 487.86
                                    return 765.13 # LEAF 121: STABLE from d8.
                            else:  # days > 6.50
                                if receipts <= 281.26:
                                    if miles <= 794.50:
                                        return 992.91 # LEAF 122: STABLE from d8.
                                    else:  # miles > 794.50
                                        return 1096.03 # LEAF 123: STABLE from d8.
                                else:  # receipts > 281.26
                                    if miles <= 731.00:
                                        return 1113.61 # LEAF 124: STABLE from d8.
                                    else:  # miles > 731.00
                                        return 1084.79 # LEAF 125: STABLE from d8.
                        else:  # receipts > 500.49
                            if miles <= 754.50:
                                if miles <= 655.50:
                                    if miles <= 625.50:
                                        return 1229.41 # LEAF 126: STABLE from d8.
                                    else:  # miles > 625.50
                                        return 1142.89 # LEAF 127: STABLE from d8.
                                else:  # miles > 655.50
                                    if receipts <= 700.28:
                                        return 1243.68 # LEAF 128: STABLE from d8.
                                    else:  # receipts > 700.28
                                        return 1216.36 # LEAF 129: STABLE from d8.
                            else:  # miles > 754.50
                                if miles <= 812.50:
                                    if receipts <= 520.60:
                                        return 1139.94 # LEAF 130: STABLE from d8.
                                    else:  # receipts > 520.60
                                        return 1122.73 # LEAF 131: STABLE from d8.
                                else:  # miles > 812.50
                                    return 1090.31 # LEAF 132: STABLE from d8.
                    else:  # days > 10.50
                        if receipts <= 552.23:
                            if days <= 12.50:
                                if miles <= 736.50:
                                    return 1113.16 # LEAF 133: STABLE from d8.
                                else:  # miles > 736.50
                                    return 1077.12 # LEAF 134: STABLE from d8.
                            else:  # days > 12.50
                                return 1396.28 # LEAF 135: STABLE from d8.
                        else:  # receipts > 552.23
                            if receipts <= 615.99:
                                return 1573.12 # LEAF 136: STABLE from d8.
                            else:  # receipts > 615.99
                                return 1487.93 # LEAF 137: STABLE from d8.
                else:  # miles > 833.50
                    if receipts <= 666.42:
                        if days <= 6.50:
                            if receipts <= 557.51:
                                if days <= 5.50:
                                    if receipts <= 414.87:
                                        return 903.82 # LEAF 138: STABLE from d8.
                                    else:  # receipts > 414.87
                                        return 1119.17 # LEAF 139: STABLE from d8.
                                else:  # days > 5.50
                                    if miles <= 1121.00:
                                        return 1133.45 # LEAF 140: STABLE from d8.
                                    else:  # miles > 1121.00
                                        return 1107.96 # LEAF 141: STABLE from d8.
                            else:  # receipts > 557.51
                                if miles <= 946.50:
                                    return 1202.46 # LEAF 142: STABLE from d8.
                                else:  # miles > 946.50
                                    if miles <= 1077.00:
                                        return 1313.95 # LEAF 143: STABLE from d8.
                                    else:  # miles > 1077.00
                                        return 1336.74 # LEAF 144: STABLE from d8.
                        else:  # days > 6.50
                            if receipts <= 447.86:
                                if receipts <= 66.01:
                                    if days <= 11.50:
                                        return 1550.55 # LEAF 145: STABLE from d8.
                                    else:  # days > 11.50
                                        return 1365.80 # LEAF 146: STABLE from d8.
                                else:  # receipts > 66.01
                                    if days <= 11.50:
                                        return 1226.45 # LEAF 147: STABLE from d8.
                                    else:  # days > 11.50
                                        return 1316.84 # LEAF 148: STABLE from d8.
                            else:  # receipts > 447.86
                                if miles <= 1136.50:
                                    if miles <= 1091.00:
                                        return 1358.28 # LEAF 149: STABLE from d8.
                                    else:  # miles > 1091.00
                                        return 1451.62 # LEAF 150: STABLE from d8.
                                else:  # miles > 1136.50
                                    return 1696.86 # LEAF 151: STABLE from d8.
                    else:  # receipts > 666.42
                        if days <= 6.50:
                            if days <= 5.50:
                                return 1375.88 # LEAF 152: STABLE from d7, d8.
                            else:  # days > 5.50
                                return 1448.72 # LEAF 153: STABLE from d7, d8.
                        else:  # days > 6.50
                            if miles <= 1170.50:
                                if receipts <= 771.86:
                                    if miles <= 887.00:
                                        return 1606.63 # LEAF 154: STABLE from d8.
                                    else:  # miles > 887.00
                                        return 1630.44 # LEAF 155: STABLE from d8.
                                else:  # receipts > 771.86
                                    return 1827.44 # LEAF 156: STABLE from d7, d8.
                            else:  # miles > 1170.50
                                return 1419.34 # LEAF 157: STABLE from d6, d7, d8.
    else:  # receipts > 828.10
        # PATH: High total receipts (> $828.10). The penalty zone.
        # TREND: THIS IS WHERE THE ACTION IS. Unlike the low-receipts branch, this branch is NOT stable.
        # The d9 tree has added significant new splits here compared to d8, indicating that the model's performance
        # jump from 10% to 20% exact matches is driven by a better understanding of these complex penalty rules.
        if days <= 5.50:
            # PATH: Short trips (<= 5.5 days) with high receipts.
            if miles <= 621.00:
                # PATH: Short trips, high receipts, low mileage.
                if receipts <= 1237.08:
                    if receipts <= 1220.09:
                        if days <= 4.50:
                            if receipts <= 1065.90:
                                if receipts <= 1029.20:
                                    if receipts <= 905.62:
                                        return 872.74 # LEAF 158: NEW LEAF. d9 splits d8's L105 ($997.39) into two, creating a lower tier. It's refining the capped reimbursement.
                                    else:  # receipts > 905.62
                                        return 1068.62 # LEAF 159: NEW LEAF. This is the higher tier of the same split.
                                else:  # receipts > 1029.20
                                    return 418.17 # LEAF 160: STABLE from d8. The severe penalty pocket remains.
                            else:  # receipts > 1065.90
                                if miles <= 124.50:
                                    if miles <= 68.00:
                                        return 922.69 # LEAF 161: NEW LEAF. d9 splits d8's L107 ($968.24) by mileage, adding more resolution to the penalty.
                                    else:  # miles > 68.00
                                        return 1013.78 # LEAF 162: NEW LEAF. The "normal" value for this path.
                                else:  # miles > 124.50
                                    if receipts <= 1211.53:
                                        return 1148.58 # LEAF 163: NEW LEAF. d9 splits d8's L108 ($1168.90) by receipt amount.
                                    else:  # receipts > 1211.53
                                        return 1229.87 # LEAF 164: NEW LEAF. Higher tier of the cap.
                        else:  # days > 4.50
                            if receipts <= 998.10:
                                if miles <= 201.00:
                                    if receipts <= 900.55:
                                        return 1050.25 # LEAF 165: NEW LEAF. d9 splits d8's L109/110 by adding a receipt tier.
                                    else:  # receipts > 900.55
                                        return 1136.67 # LEAF 166: NEW LEAF.
                                else:  # miles > 201.00
                                    if receipts <= 915.46:
                                        return 1231.67 # LEAF 167: NEW LEAF. d9 splits d8's L110 by receipt tier.
                                    else:  # receipts > 915.46
                                        return 1325.89 # LEAF 168: NEW LEAF.
                            else:  # receipts > 998.10
                                if miles <= 179.00:
                                    return 1312.16 # LEAF 169: STABLE from d8. Logic converged here.
                                else:  # miles > 179.00
                                    if miles <= 334.00:
                                        return 1485.59 # LEAF 170: NEW LEAF. d9 splits d8's L112 ($1451) by mileage.
                                    else:  # miles > 334.00
                                        return 1433.70 # LEAF 171: NEW LEAF. A mileage penalty is introduced.
                    else:  # receipts > 1220.09
                        return 511.23 # LEAF 172: STABLE from d6, d7, d8. A bedrock rule of the system.
                else:  # receipts > 1237.08
                    if miles <= 70.50:
                        if miles <= 55.00:
                            if days <= 4.50:
                                if days <= 1.50:
                                    if miles <= 23.00:
                                        return 1120.22 # LEAF 173: NEW LEAF. d9 splits d8's L114 ($1106) by mileage.
                                    else:  # miles > 23.00
                                        return 1092.94 # LEAF 174: NEW LEAF. Mileage penalty.
                                else:  # days > 1.50
                                    if days <= 3.00:
                                        return 1206.95 # LEAF 175: NEW LEAF. d9 splits d8's L115 ($1234) by duration.
                                    else:  # days > 3.00
                                        return 1261.41 # LEAF 176: NEW LEAF.
                            else:  # days > 4.50
                                if miles <= 38.50:
                                    return 1410.58 # LEAF 177: STABLE from d8.
                                else:  # miles > 38.50
                                    return 1500.28 # LEAF 178: STABLE from d8.
                        else:  # miles > 55.00
                            return 322.00 # LEAF 179: STABLE from d6, d7, d8. Bedrock penalty quirk.
                    else:  # miles > 70.50
                        if days <= 2.50:
                            if days <= 1.50:
                                if miles <= 517.50:
                                    if receipts <= 1527.61:
                                        return 1149.68 # LEAF 180: NEW LEAF. d9 splits d8's L119 by receipt amount.
                                    else:  # receipts > 1527.61
                                        return 1195.48 # LEAF 181: NEW LEAF.
                                else:  # miles > 517.50
                                    return 1295.34 # LEAF 182: STABLE from d8.
                            else:  # days > 1.50
                                if miles <= 535.00:
                                    if miles <= 259.50:
                                        return 1286.28 # LEAF 183: NEW LEAF. d9 splits d8's L121 by mileage.
                                    else:  # miles > 259.50
                                        return 1331.47 # LEAF 184: NEW LEAF.
                                else:  # miles > 535.00
                                    return 1423.86 # LEAF 185: STABLE from d8.
                        else:  # days > 2.50
                            if receipts <= 1880.42:
                                if receipts <= 1870.27:
                                    if days <= 4.50:
                                        return 1389.70 # LEAF 186: NEW LEAF. d9 splits d8's L123 by duration.
                                    else:  # days > 4.50
                                        return 1538.03 # LEAF 187: NEW LEAF.
                                else:  # receipts > 1870.27
                                    return 669.85 # LEAF 188: STABLE from d8. Penalty pocket.
                            else:  # receipts > 1880.42
                                if miles <= 455.50:
                                    if days <= 3.50:
                                        return 1417.14 # LEAF 189: NEW LEAF. d9 splits d8's L125 by duration.
                                    else:  # days > 3.50
                                        return 1490.78 # LEAF 190: NEW LEAF.
                                else:  # miles > 455.50
                                    if days <= 4.50:
                                        return 1522.36 # LEAF 191: NEW LEAF. d9 splits d8's L126 by duration.
                                    else:  # days > 4.50
                                        return 1655.51 # LEAF 192: NEW LEAF.
            else:  # miles > 621.00
                if days <= 4.50:
                    if receipts <= 1016.58:
                        if receipts <= 884.12:
                            if receipts <= 870.18:
                                if miles <= 982.00:
                                    return 1251.14 # LEAF 193: STABLE from d8.
                                else:  # miles > 982.00
                                    return 1081.05 # LEAF 194: STABLE from d8.
                            else:  # receipts > 870.18
                                return 784.52 # LEAF 195: STABLE from d7, d8. Penalty pocket.
                        else:  # receipts > 884.12
                            if days <= 3.00:
                                if miles <= 933.50:
                                    return 1144.41 # LEAF 196: STABLE from d8.
                                else:  # miles > 933.50
                                    return 1192.88 # LEAF 197: STABLE from d8.
                            else:  # days > 3.00
                                if miles <= 734.50:
                                    return 1337.63 # LEAF 198: STABLE from d8.
                                else:  # miles > 734.50
                                    return 1324.64 # LEAF 199: STABLE from d8.
                    else:  # receipts > 1016.58
                        if days <= 1.50:
                            if receipts <= 1344.48:
                                if receipts <= 1255.15:
                                    return 1346.14 # LEAF 200: STABLE from d8.
                                else:  # receipts > 1255.15
                                    if receipts <= 1291.19:
                                        return 1317.33 # LEAF 201: NEW LEAF. d9 adds a new receipt tier to d8's L135.
                                    else:  # receipts > 1291.19
                                        return 1313.53 # LEAF 202: NEW LEAF.
                            else:  # receipts > 1344.48
                                if miles <= 870.50:
                                    if receipts <= 1705.73:
                                        return 1378.32 # LEAF 203: NEW LEAF. d9 splits d8's L136 by receipt amount.
                                    else:  # receipts > 1705.73
                                        return 1415.78 # LEAF 204: NEW LEAF.
                                else:  # miles > 870.50
                                    if miles <= 1063.00:
                                        return 1460.75 # LEAF 205: NEW LEAF. d9 splits d8's L137 by mileage.
                                    else:  # miles > 1063.00
                                        return 1415.26 # LEAF 206: NEW LEAF. Mileage penalty.
                        else:  # days > 1.50
                            if days <= 3.50:
                                if miles <= 1188.00:
                                    if receipts <= 1159.47:
                                        return 1389.14 # LEAF 207: NEW LEAF. d9 splits d8's L138 by receipt amount.
                                    else:  # receipts > 1159.47
                                        return 1501.44 # LEAF 208: NEW LEAF.
                                else:  # miles > 1188.00
                                    return 1666.52 # LEAF 209: STABLE from d8.
                            else:  # days > 3.50
                                if receipts <= 2099.53:
                                    if miles <= 787.00:
                                        return 1647.26 # LEAF 210: NEW LEAF. d9 splits d8's L140 by mileage.
                                    else:  # miles > 787.00
                                        return 1555.81 # LEAF 211: NEW LEAF. Mileage penalty.
                                else:  # receipts > 2099.53
                                    if receipts <= 2293.03:
                                        return 1691.15 # LEAF 212: NEW LEAF. d9 splits d8's L141 by receipt amount.
                                    else:  # receipts > 2293.03
                                        return 1699.25 # LEAF 213: NEW LEAF.
                else:  # days > 4.50
                    if receipts <= 1120.38:
                        if receipts <= 920.07:
                            if miles <= 999.00:
                                if miles <= 767.00:
                                    return 1468.46 # LEAF 214: STABLE from d8.
                                else:  # miles > 767.00
                                    if receipts <= 885.96:
                                        return 1502.49 # LEAF 215: NEW LEAF. d9 splits d8's L143 by receipt.
                                    else:  # receipts > 885.96
                                        return 1499.68 # LEAF 216: NEW LEAF.
                            else:  # miles > 999.00
                                return 1430.04 # LEAF 217: STABLE from d8.
                        else:  # receipts > 920.07
                            if receipts <= 991.52:
                                if miles <= 825.50:
                                    return 1608.60 # LEAF 218: STABLE from d8.
                                else:  # miles > 825.50
                                    return 1676.48 # LEAF 219: STABLE from d8.
                            else:  # receipts > 991.52
                                if miles <= 703.50:
                                    return 1465.26 # LEAF 220: STABLE from d8.
                                else:  # miles > 703.50
                                    return 1492.08 # LEAF 221: STABLE from d8.
                    else:  # receipts > 1120.38
                        if receipts <= 2383.49:
                            if receipts <= 2282.02:
                                if receipts <= 1173.62:
                                    return 1654.62 # LEAF 222: STABLE from d8.
                                else:  # receipts > 1173.62
                                    if miles <= 808.50:
                                        return 1745.46 # LEAF 223: NEW LEAF. d9 splits d8's L150 by mileage.
                                    else:  # miles > 808.50
                                        return 1706.46 # LEAF 224: NEW LEAF. Mileage penalty.
                            else:  # receipts > 2282.02
                                if miles <= 949.50:
                                    if receipts <= 2356.43:
                                        return 1791.96 # LEAF 225: NEW LEAF. d9 splits d8's L151 by receipt.
                                    else:  # receipts > 2356.43
                                        return 1785.53 # LEAF 226: NEW LEAF.
                                else:  # miles > 949.50
                                    return 1743.85 # LEAF 227: STABLE from d8.
                        else:  # receipts > 2383.49
                            if miles <= 1100.50:
                                if miles <= 929.00:
                                    return 1643.96 # LEAF 228: STABLE from d8.
                                else:  # miles > 929.00
                                    if miles <= 1082.50:
                                        return 1664.76 # LEAF 229: NEW LEAF. d9 splits d8's L154.
                                    else:  # miles > 1082.50
                                        return 1664.83 # LEAF 230: NEW LEAF.
                            else:  # miles > 1100.50
                                return 1711.97 # LEAF 231: STABLE from d8.
        else:  # days > 5.50
            # PATH: Longer trips (6+ days) with high receipts (> $828.10).
            # TREND: Just like the short, high-receipts branch, this is where the d9 tree uses its extra depth.
            # Nearly every leaf from the d8 tree has been split further, adding more resolution to the penalty calculations.
            if miles <= 693.00:
                # PATH: Longer trips, high receipts, low mileage.
                if receipts <= 1155.65:
                    if receipts <= 947.01:
                        if receipts <= 938.48:
                            if miles <= 407.00:
                                if days <= 11.00:
                                    if receipts <= 925.57:
                                        return 1152.64 # LEAF 232: NEW LEAF. d9 splits d8's L156.
                                    else:  # receipts > 925.57
                                        return 1262.03 # LEAF 233: NEW LEAF.
                                else:  # days > 11.00
                                    if receipts <= 879.83:
                                        return 1377.35 # LEAF 234: NEW LEAF. d9 splits d8's L157.
                                    else:  # receipts > 879.83
                                        return 1371.86 # LEAF 235: NEW LEAF.
                            else:  # miles > 407.00
                                if days <= 11.50:
                                    if miles <= 587.00:
                                        return 1323.21 # LEAF 236: NEW LEAF. d9 splits d8's L158.
                                    else:  # miles > 587.00
                                        return 1390.22 # LEAF 237: NEW LEAF.
                                else:  # days > 11.50
                                    return 1492.64 # LEAF 238: STABLE from d8.
                        else:  # receipts > 938.48
                            return 877.17 # LEAF 239: STABLE from d6,d7,d8. Penalty pocket.
                    else:  # receipts > 947.01
                        if miles <= 381.00:
                            if days <= 11.50:
                                if receipts <= 1096.43:
                                    if receipts <= 1048.36:
                                        return 1340.03 # LEAF 240: NEW LEAF. d9 splits d8's L161.
                                    else:  # receipts > 1048.36
                                        return 1399.82 # LEAF 241: NEW LEAF.
                                else:  # receipts > 1096.43
                                    if days <= 9.00:
                                        return 1478.56 # LEAF 242: NEW LEAF. d9 splits d8's L162.
                                    else:  # days > 9.00
                                        return 1527.76 # LEAF 243: NEW LEAF.
                            else:  # days > 11.50
                                if receipts <= 1073.78:
                                    if miles <= 259.00:
                                        return 1504.73 # LEAF 244: NEW LEAF. d9 splits d8's L163.
                                    else:  # miles > 259.00
                                        return 1432.75 # LEAF 245: NEW LEAF.
                                else:  # receipts > 1073.78
                                    if receipts <= 1103.04:
                                        return 1703.02 # LEAF 246: NEW LEAF. d9 splits d8's L164.
                                    else:  # receipts > 1103.04
                                        return 1525.14 # LEAF 247: NEW LEAF.
                        else:  # miles > 381.00
                            if receipts <= 985.79:
                                return 1656.28 # LEAF 248: STABLE from d8. Jackpot pocket.
                            else:  # receipts > 985.79
                                if receipts <= 1000.17:
                                    return 1395.03 # LEAF 249: STABLE from d8.
                                    return 1518.43 # LEAF 250: NEW LEAF. d9 splits d8's L167.
                                else:  # receipts > 1000.17
                                    if days <= 10.00:
                                        return 1518.43 # LEAF 250: NEW LEAF. d9 splits d8's L167.
                                    else:  # days > 10.00
                                        return 1630.47 # LEAF 251: NEW LEAF.
                else:  # receipts > 1155.65
                    if days <= 10.50:
                        if miles <= 622.00:
                            if receipts <= 1427.37:
                                if receipts <= 1407.23:
                                    if days <= 8.50:
                                        return 1508.05 # LEAF 252: NEW LEAF. d9 splits d8's L168.
                                    else:  # days > 8.50
                                        return 1562.53 # LEAF 253: NEW LEAF.
                                else:  # receipts > 1407.23
                                    return 631.81 # LEAF 254: STABLE from d8. Extreme penalty pocket.
                            else:  # receipts > 1427.37
                                if miles <= 107.50:
                                    if miles <= 11.00:
                                        return 1422.12 # LEAF 255: NEW LEAF. d9 splits d8's L170.
                                    else:  # miles > 11.00
                                        return 1474.64 # LEAF 256: NEW LEAF.
                                else:  # miles > 107.50
                                    if miles <= 293.50:
                                        return 1560.39 # LEAF 257: NEW LEAF. d9 splits d8's L171.
                                    else:  # miles > 293.50
                                        return 1617.75 # LEAF 258: NEW LEAF.
                        else:  # miles > 622.00
                            if miles <= 632.00:
                                if receipts <= 1456.05:
                                    return 1730.86 # LEAF 259: STABLE from d8.
                                else:  # receipts > 1456.05
                                    if receipts <= 1792.71:
                                        return 1800.86 # LEAF 260: NEW LEAF. d9 splits d8's L173.
                                    else:  # receipts > 1792.71
                                        return 1739.49 # LEAF 261: NEW LEAF.
                            else:  # miles > 632.00
                                if days <= 6.50:
                                    return 1796.98 # LEAF 262: STABLE from d8.
                                else:  # days > 6.50
                                    if miles <= 686.50:
                                        return 1635.99 # LEAF 263: NEW LEAF. d9 splits d8's L175.
                                    else:  # miles > 686.50
                                        return 1706.11 # LEAF 264: NEW LEAF.
                    else:  # days > 10.50
                        if days <= 12.50:
                            if miles <= 227.50:
                                if miles <= 28.50:
                                    if receipts <= 2245.21:
                                        return 1567.13 # LEAF 265: NEW LEAF. d9 splits d8's L176.
                                    else:  # receipts > 2245.21
                                        return 1556.78 # LEAF 266: NEW LEAF.
                                else:  # miles > 28.50
                                    if miles <= 65.50:
                                        return 1661.51 # LEAF 267: NEW LEAF. d9 splits d8's L177.
                                    else:  # miles > 65.50
                                        return 1586.41 # LEAF 268: NEW LEAF.
                            else:  # miles > 227.50
                                if miles <= 462.00:
                                    if days <= 11.50:
                                        return 1657.58 # LEAF 269: NEW LEAF. d9 splits d8's L178.
                                    else:  # days > 11.50
                                        return 1737.58 # LEAF 270: NEW LEAF.
                                else:  # miles > 462.00
                                    if receipts <= 2348.90:
                                        return 1761.17 # LEAF 271: NEW LEAF. d9 splits d8's L179.
                                    else:  # receipts > 2348.90
                                        return 1658.29 # LEAF 272: NEW LEAF.
                        else:  # days > 12.50
                            if miles <= 257.00:
                                if miles <= 96.50:
                                    return 1682.62 # LEAF 273: STABLE from d8.
                                else:  # miles > 96.50
                                    if miles <= 118.50:
                                        return 1807.67 # LEAF 274: NEW LEAF. d9 splits d8's L181.
                                    else:  # miles > 118.50
                                        return 1743.96 # LEAF 275: NEW LEAF.
                            else:  # miles > 257.00
                                if miles <= 522.50:
                                    if receipts <= 2051.80:
                                        return 1857.32 # LEAF 276: NEW LEAF. d9 splits d8's L182.
                                    else:  # receipts > 2051.80
                                        return 1968.40 # LEAF 277: NEW LEAF.
                                else:  # miles > 522.50
                                    if miles <= 537.50:
                                        return 2047.16 # LEAF 278: NEW LEAF. d9 splits d8's L183.
                                    else:  # miles > 537.50
                                        return 1956.06 # LEAF 279: NEW LEAF.
            else:  # miles > 693.00
                if miles <= 940.50:
                    if miles <= 845.50:
                        if miles <= 726.50:
                            if miles <= 700.00:
                                return 1815.02 # LEAF 280: STABLE from d8.
                            else:  # miles > 700.00
                                if miles <= 707.00:
                                    return 2030.59 # LEAF 281: STABLE from d8.
                                else:  # miles > 707.00
                                    if days <= 12.50:
                                        return 1884.93 # LEAF 282: NEW LEAF. d9 splits d8's L186.
                                    else:  # days > 12.50
                                        return 1980.41 # LEAF 283: NEW LEAF.
                        else:  # miles > 726.50
                            if miles <= 740.50:
                                if miles <= 737.00:
                                    return 1792.31 # LEAF 284: STABLE from d8.
                                else:  # miles > 737.00
                                    return 902.09 # LEAF 285: STABLE from d8. Penalty pocket.
                            else:  # miles > 740.50
                                if days <= 9.50:
                                    if miles <= 763.50:
                                        return 1893.56 # LEAF 286: NEW LEAF. d9 splits d8's L189.
                                    else:  # miles > 763.50
                                        return 1655.16 # LEAF 287: NEW LEAF.
                                else:  # days > 9.50
                                    if receipts <= 1183.29:
                                        return 1745.05 # LEAF 288: NEW LEAF. d9 splits d8's L190.
                                    else:  # receipts > 1183.29
                                        return 1862.58 # LEAF 289: NEW LEAF.
                    else:  # miles > 845.50
                        if receipts <= 2098.61:
                            if miles <= 925.50:
                                if days <= 10.50:
                                    if receipts <= 1279.70:
                                        return 1909.64 # LEAF 290: NEW LEAF. d9 splits d8's L191.
                                    else:  # receipts > 1279.70
                                        return 1815.86 # LEAF 291: NEW LEAF.
                                else:  # days > 10.50
                                    if receipts <= 979.79:
                                        return 1857.18 # LEAF 292: NEW LEAF. d9 splits d8's L192.
                                    else:  # receipts > 979.79
                                        return 1958.74 # LEAF 293: NEW LEAF.
                            else:  # miles > 925.50
                                if days <= 11.50:
                                    if receipts <= 1650.35:
                                        return 1804.68 # LEAF 294: NEW LEAF. d9 splits d8's L193.
                                    else:  # receipts > 1650.35
                                        return 1779.12 # LEAF 295: NEW LEAF.
                                else:  # days > 11.50
                                    return 1663.58 # LEAF 296: STABLE from d8.
                        else:  # receipts > 2098.61
                            if receipts <= 2457.39:
                                if miles <= 880.00:
                                    if miles <= 866.00:
                                        return 1759.97 # LEAF 297: NEW LEAF. d9 splits d8's L195.
                                    else:  # miles > 866.00
                                        return 1776.62 # LEAF 298: NEW LEAF.
                                else:  # miles > 880.00
                                    if miles <= 900.50:
                                        return 1718.71 # LEAF 299: STABLE from d8.
                                    else:  # miles > 900.50
                                        return 1751.49 # LEAF 300: NEW LEAF. d9 splits d8's L196.
                            else:  # receipts > 2457.39
                                return 1885.87 # LEAF 301: STABLE from d8.
                else:  # miles > 940.50
                    if receipts <= 1830.24:
                        if receipts <= 866.87:
                            if days <= 8.50:
                                return 1699.90 # LEAF 302: STABLE from d7, d8.
                            else:  # days > 8.50
                                if miles <= 1089.00:
                                    return 1865.67 # LEAF 303: STABLE from d8.
                                else:  # miles > 1089.00
                                    return 1797.14 # LEAF 304: STABLE from d8.
                        else:  # receipts > 866.87
                            if days <= 6.50:
                                if miles <= 1095.50:
                                    if receipts <= 1312.03:
                                        return 1803.97 # LEAF 305: NEW LEAF. d9 splits d8's L201.
                                    else:  # receipts > 1312.03
                                        return 1807.42 # LEAF 306: NEW LEAF.
                                else:  # miles > 1095.50
                                    return 1776.48 # LEAF 307: STABLE from d8.
                            else:  # days > 6.50
                                if miles <= 1017.50:
                                    if days <= 7.50:
                                        return 2086.82 # LEAF 308: NEW LEAF. d9 splits d8's L203.
                                    else:  # days > 7.50
                                        return 1942.29 # LEAF 309: NEW LEAF.
                                else:  # miles > 1017.50
                                    if days <= 8.50:
                                        return 2012.76 # LEAF 310: NEW LEAF. d9 splits d8's L204.
                                    else:  # days > 8.50
                                        return 2159.39 # LEAF 311: NEW LEAF.
                    else:  # receipts > 1830.24
                        if days <= 12.50:
                            if miles <= 1167.50:
                                if receipts <= 2325.01:
                                    if miles <= 1131.50:
                                        return 1836.71 # LEAF 312: NEW LEAF. d9 splits d8's L205.
                                    else:  # miles > 1131.50
                                        return 1755.76 # LEAF 313: NEW LEAF.
                                else:  # receipts > 2325.01
                                    if receipts <= 2399.31:
                                        return 1740.06 # LEAF 314: NEW LEAF. d9 splits d8's L206.
                                    else:  # receipts > 2399.31
                                        return 1798.90 # LEAF 315: NEW LEAF.
                            else:  # miles > 1167.50
                                if miles <= 1189.50:
                                    return 1921.16 # LEAF 316: STABLE from d8.
                                else:  # miles > 1189.50
                                    return 1972.88 # LEAF 317: STABLE from d8.
                        else:  # days > 12.50
                            if receipts <= 2055.23:
                                return 1997.52 # LEAF 318: STABLE from d8.
                            else:  # receipts > 2055.23
                                if miles <= 1045.00:
                                    return 1842.24 # LEAF 319: STABLE from d8.
                                else:  # miles > 1045.00
                                    if miles <= 1171.00:
                                        return 1899.78 # LEAF 320: NEW LEAF. d9 splits d8's L211.
                                    else:  # miles > 1171.00
                                        return 1924.80 # LEAF 321: NEW LEAF.

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print("Usage: python calculate_reimbursement_hybrid.py <days> <miles> <receipts>")
        sys.exit(1)

    try:
        # FIX: Strip whitespace (like \r) from args to prevent parsing errors,
        # and ensure miles are correctly parsed as a float.
        days_arg = int(sys.argv[1].strip())
        miles_arg = float(sys.argv[2].strip())
        receipts_arg = float(sys.argv[3].strip())
    except (ValueError, IndexError):
        print("Invalid input. Please provide numeric values for days, miles, and receipts.", file=sys.stderr)
        sys.exit(1)

    reimbursement = tree_depth_9(days_arg, miles_arg, receipts_arg)
    print(reimbursement)
