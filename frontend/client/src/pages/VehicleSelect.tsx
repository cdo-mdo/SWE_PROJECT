import { VehicleCard } from "@/components/VehicleCard";
import { useQuery } from "@tanstack/react-query";
import { getCars } from "@/lib/api";
import { Skeleton } from "@/components/ui/skeleton";

// Car type mapping functions
function getCarTypeName(typeId: number): string {
  const types = {
    1: "Economy Sedan",
    2: "Luxury Sedan",
    3: "SUV",
    4: "Sports Car",
    5: "Van"
  };
  return types[typeId as keyof typeof types] || `Car Type ${typeId}`;
}

function getCarPrice(typeId: number): number {
  const prices = {
    1: 50,
    2: 100,
    3: 80,
    4: 150,
    5: 90
  };
  return prices[typeId as keyof typeof prices] || 70;
}

function getCarCapacity(typeId: number): number {
  const capacity = {
    1: 4,
    2: 4,
    3: 7,
    4: 2,
    5: 8
  };
  return capacity[typeId as keyof typeof capacity] || 4;
}

function getCarLuggage(typeId: number): number {
  const luggage = {
    1: 2,
    2: 3,
    3: 4,
    4: 1,
    5: 5
  };
  return luggage[typeId as keyof typeof luggage] || 2;
}

function getCarImage(typeId: number): string {
  const images = {
    1: "https://images.unsplash.com/photo-1541899481282-d53bffe3c35d?ixlib=rb-4.0.3",
    2: "https://images.unsplash.com/photo-1563720223185-11003d516935?ixlib=rb-4.0.3",
    3: "https://images.unsplash.com/photo-1551830820-330a71b99659?ixlib=rb-4.0.3",
    4: "https://images.unsplash.com/photo-1544829099-b9a0c07fad1a?ixlib=rb-4.0.3",
    5: "https://images.unsplash.com/photo-1559416523-140ddc3d238c?ixlib=rb-4.0.3"
  };
  return images[typeId as keyof typeof images] || images[1];
}

export default function VehicleSelect() {
  const { data, isLoading, error } = useQuery({ queryKey: ['cars'], queryFn: getCars });

  if (error) {
    return <div className="text-center text-red-500 mt-8">Failed to load vehicles</div>;
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 py-4 sm:px-6 lg:px-8">
        <img
            src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTv8VCDlM64uFv7274Mn3UjHpqXRGtIwAWokg&s"
            alt="Rent logo"
            className="h-12 cursor-pointer"
            onClick={() => window.location.href = '/'}
          />
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 py-12 sm:px-6 lg:px-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-8">
          Select Your Vehicle
        </h1>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {isLoading ? (
            Array(6).fill(0).map((_, index) => (
              <Skeleton key={index} className="h-[400px] w-full rounded-xl" />
            ))
          ) : (
            data?.cars.map((car) => (
              <VehicleCard
                key={car.id}
                vehicle={{
                  id: car.id,
                  name: getCarTypeName(car.car_type_id),
                  description: `License: ${car.license_plate}`,
                  price: getCarPrice(car.car_type_id),
                  capacity: getCarCapacity(car.car_type_id),
                  luggage: getCarLuggage(car.car_type_id),
                  transmission: "Automatic",
                  image: getCarImage(car.car_type_id),
                  status: car.status,
                  mileage: car.mileage
                }}
              />
            ))
          )}
        </div>
      </main>
    </div>
  );
}