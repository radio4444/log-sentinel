import * as fs from "fs";
import {z} from "zod";

// read file -> convert to JS object -> run through zod

// Define SummarySchema from cleaned_metrics
const SummarySchema = z.object({
    total_valid_logs: z.number().int(),
    "Average Response time": z.number(),
    total_error_counts: z.number().int()

})

// Define ErrorlogScheme from cleaned_metrics
const ErrorLogSchema = z.object({
    timestamp: z.string(),
    log_level: z.string(),
    status_code: z.number().int(),
    response_time_in_ms: z.number()
})

// Define CleanedMetrics Schema from cleaned_metrics
const CleanedMetricsSchema = z.object({
    summary: SummarySchema,
    flagged_errors: z.array(ErrorLogSchema)
})

// Load raw cleaned_metrics.json file
try {
    const rawCleanedMetrics = fs.readFileSync("json/cleaned_metrics.json", "utf-8")
    // Parse raw into JSONobject
    const jsonCleanedMetrics = JSON.parse(rawCleanedMetrics)
    // validate jsonCleanedMetrics data by Zod 
    CleanedMetricsSchema.parse(jsonCleanedMetrics)
    // console.log("Validation successful!")


} catch (error) {
    if (error instanceof Error) {
        console.error(error.message)
    } else {
        console.error("An unknown error occured: ", error)
    }
}