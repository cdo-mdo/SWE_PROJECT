import { SearchForm } from "@/components/SearchForm";
import { VehicleCard } from "@/components/VehicleCard";
import { useQuery } from "@tanstack/react-query";
import { Car, getCars } from "@/lib/api";
import { z } from "zod";
import { Skeleton } from "@/components/ui/skeleton";
import type { VehicleCardProps } from "@/components/VehicleCard";

// Define the type for the API response - this matches what getCars returns
type CarsResponse = {
  cars: Car[];
};

export default function Home() {
  const { data, isLoading, error } = useQuery<CarsResponse>({
    queryKey: ["cars"],
    queryFn: async () => {
      try {
        const response = await getCars();
        if (!response?.cars?.length) {
          throw new Error("No cars data available");
        }
        return response;
      } catch (err) {
        console.error("Failed to fetch cars:", err);
        throw err;
      }
    },
    retry: 3,
    staleTime: 5 * 60 * 1000 // 5 minutes
  });

  const transformCarData = (car: Car): VehicleCardProps["vehicle"] => ({
    id: car.id,
    name: getCarTypeName(car.car_type_id),
    description: `License: ${car.license_plate}`,
    price: getCarPrice(car.car_type_id),
    capacity: getCarCapacity(car.car_type_id),
    luggage: getCarLuggage(car.car_type_id),
    transmission: "Automatic",
    image: `https://source.unsplash.com/random/800x600/?car,${car.car_type_id}`,
    status: car.status,
    mileage: car.mileage
  });

  type CarTypeInfo = {
    name: string;
    price: number;
    capacity: number;
    luggage: number;
  };

  const carTypes: Record<number, CarTypeInfo> = {
    1: { name: "Economy Sedan", price: 50, capacity: 4, luggage: 2 },
    2: { name: "Luxury Sedan", price: 100, capacity: 4, luggage: 3 },
    3: { name: "SUV", price: 80, capacity: 7, luggage: 4 },
    4: { name: "Sports Car", price: 150, capacity: 2, luggage: 1 },
    5: { name: "Van", price: 90, capacity: 8, luggage: 5 }
  };

  function getCarTypeName(typeId: number): string {
    return carTypes[typeId]?.name || `Car Type ${typeId}`;
  }

  function getCarPrice(typeId: number): number {
    return carTypes[typeId]?.price || 70;
  }

  function getCarCapacity(typeId: number): number {
    return carTypes[typeId]?.capacity || 4;
  }

  function getCarLuggage(typeId: number): number {
    return carTypes[typeId]?.luggage || 2;
  }
  return (
    <div className="min-h-screen bg-gradient-to-b from-blue-50 to-white">
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 py-4 sm:px-6 lg:px-8 flex items-center">
          <img
            src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTv8VCDlM64uFv7274Mn3UjHpqXRGtIwAWokg&s"
            alt="Rent logo"
            className="h-12 cursor-pointer"
            onClick={() => window.location.href = '/'}
          />
        </div>
      </header>

      <main>
        <div className="max-w-7xl mx-auto px-4 py-12 sm:px-6 lg:px-8">
          <div className="text-center mb-12">
            <h1 className="text-4xl font-bold text-gray-900 mb-4">
              Find Your Perfect Rental Car
            </h1>
            <p className="text-lg text-gray-600">
              Choose from a wide selection of vehicles at competitive rates
            </p>
          </div>

          <SearchForm />

          <div className="mt-24">
            <h2 className="text-3xl font-bold text-gray-900 mb-8 text-center">
              Featured Vehicles
            </h2>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
              {isLoading ? (
                [...Array(3)].map((_, index) => (
                  <div key={index} className="space-y-4">
                    <Skeleton className="h-48 w-full" />
                    <Skeleton className="h-4 w-3/4" />
                    <Skeleton className="h-4 w-1/2" />
                  </div>
                ))
              ) : error ? (
                <div className="col-span-3 text-center text-red-500">
                  Error loading vehicles. Please try again later.
                </div>
              ) : data?.cars ? (
                data.cars.slice(0, 3).map((car) => (
                  <VehicleCard
                    key={car.id}
                    vehicle={transformCarData(car)}
                  />
                ))
              ) : null}
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}