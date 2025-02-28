import { SearchForm } from "@/components/SearchForm";
import { VehicleCard } from "@/components/VehicleCard";
import { vehicles } from "@/lib/mockData";

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-b from-blue-50 to-white">
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 py-4 sm:px-6 lg:px-8 flex items-center">
          <img
            src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTv8VCDlM64uFv7274Mn3UjHpqXRGtIwAWokg&s"
            alt="Rent logo"
            className="h-12"
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
              {vehicles.slice(0, 3).map((vehicle) => (
                <VehicleCard
                  key={vehicle.id}
                  vehicle={vehicle}
                />
              ))}
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}