import marimo

__generated_with = "0.19.9"
app = marimo.App(width="full")


@app.cell
def _():
    a= 15
    return (a,)


@app.cell
def _(a):
    b = a* 2
    print(b)
    return


@app.cell
def _():
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            less = [i for i in arr[1:] if i <= pivot]
            greater = [i for i in arr[1:] if i > pivot]
            return quick_sort(less) + [pivot] + quick_sort(greater)


    l = list([5, 2, 8, 1, 9, 4])
    print(quick_sort(l))
    return


if __name__ == "__main__":
    app.run()
