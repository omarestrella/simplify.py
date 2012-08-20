### simplify.py

simplify.py is a simple port of simplify.js by Vladimir Agafonkin ([https://github.com/mourner/simplify-js](https://github.com/mourner/simplify-js))

### Usage

```
import simplify
simplify(points, tolerance, highQuality)
```


`points`: An array of dictionaries, containing x, y coordinates: `{'x': int/float, 'y': int/float}`

`tolerance (optional, 0.1 by default)`: Affects the amount of simplification that occurs (the smaller, the less simplification).

`highestQuality (options, True by default)`: Flag to exclude the distance pre-processing. Produces higher quality results, but runs slower.