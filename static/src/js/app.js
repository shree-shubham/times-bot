$(function() {
    var rates = [];
    var averageRate;
    var stdDevRate;

    /**
     * Math Helpers
     **/

    /**
     * _standardDeviation and _average methods taken from:
     * http://derickbailey.com/2014/09/21/calculating-standard-deviation-with-array-map-and-array-reduce-in-javascript/
     **/
    function _average(data){
      var sum = data.reduce(function(sum, value) {
        return sum + value;
      }, 0);

      var avg = sum / data.length;
      return avg;
    }

    /**
     * _standardDeviation and _average methods taken from:
     * http://derickbailey.com/2014/09/21/calculating-standard-deviation-with-array-map-and-array-reduce-in-javascript/
     **/
    function _standardDeviation(values){
      var avg = _average(values);

      var squareDiffs = values.map(function(value) {
        var diff = value - avg;
        var sqrDiff = diff * diff;
        return sqrDiff;
      });

      var avgSquareDiff = _average(squareDiffs);

      var stdDev = Math.sqrt(avgSquareDiff);
      return stdDev;
    }

    /**
     * refreshData
     *
     * Polls the API for the current comment rate, entropy, and probabilty,
     * inserting those values into the DOM as needed.  This will also print a
     * message if the rate is more than one standard deviation away from the
     * standard rate.
     **/
    function refreshData() {

        // Get the rate
        $.getJSON('/rate').success(function(data) {

            // Compute the average rate seen in the past 10 rates, as well as
            // the standard deviation.
            var rate = data.data.rate;
            rates.push(rate);

            while (rates.length > 10) {
                rates.shift();
            }

            averageRate = _average(rates);
            stdDevRate = _standardDeviation(rates);

            // Compute the deviation for this data point.
            var deviation = rate - averageRate;

            // Show the rate onscreen.
            $('#rate').text(rate.toFixed(2));

            // If the rate is more than one std dev in either direction,
            // display a message indicating this.
            if (Math.abs(deviation) > stdDevRate) {
                $('#message')
                    .text('Whoa, that\'s ' + deviation + ' standard ' +
                        'deviations ' + (deviation > 0 ? 'above' : 'below') + ' the averge.')
                    .slideDown();
            } else {
                $('#message').slideUp();
            }
        });

        // Get the entropy value from the API and put it in the page.
        $.getJSON('/entropy').success(function(data) {
            var entropy = data.data.entropy.toFixed(2);
            $('#entropy').text(entropy);
        });

        // Get the probability value that there will be a comment in the next
        // 30 seconds from the API and put it in the page.
        $.getJSON('/probability/30').success(function(data) {
            var probability = (data.data.probability * 100).toFixed(2);
            console.log(probability);
            $('#probability').text(probability + "%");
        });

        // Call refreshData infinitely, once every 2 seconds.
        setTimeout(refreshData, 2000);
    }

    // Initial call to get everything started.
    refreshData();
});
