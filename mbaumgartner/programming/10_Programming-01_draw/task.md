You are given a class `Canvas` which represents a rectangular drawing area. Read the source code and comments provided in the code template to understand how.

Then, implement the `draw` method, which essentially moves a "pencil" across the canvas, drawing a sequence of adjacent pixels one by one.

`draw` takes four parameters:

 * `x` a starting x (horizontal) coordinate
 * `y` a starting y (vertical) coordinate
 * `path` a string containing a sequence of up (`"u"`), down (`"d"`), left (`"l"`), and right (`"r"`)  movements represented by the given characters (`""` by default)
 * `char` a single character used to paint on the canvas (`"█"` by default)

`draw` first places the "pencil" at the provided `x`/`y` coordinates and draws `char` at that location. Then, it goes through the movement instructions one by one to update the pencil coordinates. Thus, if `path` is the empty string, only a single pixel is drawn (at the `x`/`y` coordinates). In the general case, `len(path)+1` pixels are drawn. The top-left-most pixel is at coordinates `0`/`0`.

With regard to possible arguments to `draw`, `draw` should be generous in what it accepts. It should...

 * ...not care about casing ("d" vs. "D") in the `path` string
 * ...silently ignore `path` characters which are not valid movement instructions, rather than fail
 * ...wrap around the edges of the canvas if the pencil is placed or moved out of bounds, rather than fail
 * ...allow over-writing pixels multiple times

On the other hand, `draw` should raise an `Exception` if...

 * ...`x` or `y` is not an integer
 * ...`path` is not a string
 * ...`char` is not a string or has any length other than `1`

You must implement `draw`. You may add additional methods to the class if you want; but you don't have to.

**Important**: Do **not** modify the already implementated methods of `Canvas`!

**Important**: Do **not** add any additional top-level definitions (except for imports, if you need any). Your solution must be contained entirely inside `Canvas`!

**Important**: Do **not** modify the signature already provided for `draw`!

**Important**: Hand in your **entire** class definition, including the signature and the methods provided in the template! In case you need any imports, include them, too.
