# API

## URL format

The API is accessed at:

/classify-perfect-number?number=***query***

## Arguments

The API accepts the following argument:
  * number: a positive integer

## Outputs

The API returns the following as a json object:
  * **input**: the orginal query

  * When classification has not been possible: **error - **details of why it has not been possible to classify the input 

  * When classification has been possible: **classification** - either

    * perfect - if the query is a perfect number 
    * abundant - if the query is an abundant number


    * deficient  - if the query is a deficient number

