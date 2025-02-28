import { z } from "zod";

export const locationSchema = z.object({
  id: z.string(),
  name: z.string(),
  address: z.string(),
  city: z.string(),
  state: z.string(),
  zip: z.string(),
  image: z.string()
});

export const vehicleCategorySchema = z.object({
  id: z.string(),
  name: z.string(),
  description: z.string(),
  capacity: z.number(),
  luggage: z.number(),
  transmission: z.enum(["Automatic", "Manual"]),
  price: z.number(),
  image: z.string()
});

export const searchFormSchema = z.object({
  pickupLocation: z.string(),
  dropoffLocation: z.string(),
  pickupDate: z.date(),
  dropoffDate: z.date(),
  pickupTime: z.string(),
  dropoffTime: z.string()
});

export type Location = z.infer<typeof locationSchema>;
export type VehicleCategory = z.infer<typeof vehicleCategorySchema>;
export type SearchFormData = z.infer<typeof searchFormSchema>;
