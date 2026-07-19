
# Key Takeaways:
#
# (1) Detect the calculation part that can generate float value
#     and avoid the part which leads to float type.
#
#     In this example, the core part is "W / H / H".
#     Therefore, "W / H / H >= (25 * 100 * 100)" cannot
#     achieve AC and "W * 100 * 100 / H / H" is the expression
#     to avoid calculation errors.

H, W = map(int, input().split())

if (W * 100 * 100 / (H ** 2)) >= 25.0:
    print("Yes")
else:
    print("No")
