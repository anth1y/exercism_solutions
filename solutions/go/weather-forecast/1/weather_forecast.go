/* Package weather provides tools to provide the weather condition in your location. */
package weather
// CurrentCondition will hold the value of the current weather condition.
var CurrentCondition string
// CurrentLocation will hold the value of the city.
var CurrentLocation string

// Forecast function will provide you with the weather condition of your location.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
