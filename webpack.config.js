var path = require("path")
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
  context: __dirname,

  entry: './assets/src/index', // entry point of react app, all roads lead to index.js
  output: {
    path: path.resolve('./assets/bundles/'),
    filename: "[name]-[hash].js",
  },

  plugins: [
    new BundleTracker({filename: './webpack-stats.json'}),
  ],

  module: {
    loaders: [
      { test: /.jsx?$/, loader: 'babel-loader', exclude: /node_modules/,query: {presets: ['es2015','react']}}, // This transforms JSX in JS, so older engines can render our app
    ],
  },

  resolve: {
     modules: ['node_modules','bower_components'],
    extensions: ['.js','.jsx']
  },
}
